import gym
import time
import keyboard
import math
import random
import matplotlib.pyplot as plt


class QLearning:
    def __init__(self):
        self.exploration = 0.6
        self.learning_rate = 0.3
        self.discount_rate = 0.99
        self.degrees = [2 * math.pi * x / 360 for x in range(360)]
        self.state_matrix = dict()

    def set_exploration(self, rate):
        self.exploration = rate

    def set_learning_rate(self, rate):
        self.learning_rate = rate

    def set_discount_rate(self, rate):
        self.discount_rate = rate

    # Choosing a random action or the best action depending on rand_num
    def get_action(self, state):
        rand_num = random.randint(0, 100)
        self.state_matrix[state] = self.state_matrix.get(state, [0, 0])

        if rand_num <= 100 * self.exploration:
            return random.randint(0, 1)

        return 0 if self.state_matrix[state][0] > self.state_matrix[state][1] else 1

    # Updating the q-value
    def update_q_value(self, prev_state, prev_action, new_state, reward, done):
        self.state_matrix[prev_state] = self.state_matrix.get(prev_state, [0, 0])
        self.state_matrix[new_state] = self.state_matrix.get(new_state, [0, 0])
        if not done:
            learned_value = self.learning_rate * (reward + self.discount_rate
                                                  * max(self.state_matrix[new_state][0],
                                                        self.state_matrix[new_state][1])
                                                  - self.state_matrix[prev_state][prev_action])
        else:
            learned_value = self.learning_rate * reward
        self.state_matrix[prev_state][prev_action] += learned_value

    # Returning the current state given the input parameters
    def get_state(self, pos, velocity, angle, ang_vel):
        # The different discretizations of the parameters
        pos_splits = [-1.5, -1, -0.5, 0, 0.5, 1.5]
        velocity_splits = [-1, -0.5, 0, 0.5, 1]
        angle_splits = [-self.degrees[9], -self.degrees[6], -self.degrees[3], self.degrees[0], self.degrees[3],
                        self.degrees[6], self.degrees[9]]
        angle_vel_splits = [-1, -0.7, -0.3, -0.1, 0, 0.1, 0.3, 0.7, 1]
        parameters = [pos_splits, velocity_splits, angle_splits, angle_vel_splits]
        inp_parameters = [pos, velocity, angle, ang_vel]
        state = "|"

        # Creating the state string
        # state=_pos|velocity|angle|angelVelocity|
        for x in range(len(parameters)):
            for y in range(len(parameters[x])):
                if inp_parameters[x] < parameters[x][y]:
                    state += str(parameters[x][y])
                    break
            state += str("|")
        return state


def add_point(frames):
    frames_vector.append(frames)
    pos_vector.append(len(frames_vector))

    # Updating the graph every 500 session
    if len(pos_vector) % 500 == 0:
        plt.close()
        plt.plot(pos_vector, frames_vector)
        plt.show()
        plt.pause(0.0001)


# Setting up the agent and the environment
env = gym.make('CartPole-v1')
agent = QLearning()
highest_score = 0
abort_rendering = False  # never rendering the game if set to true
rendering = False  # the key for rendering is pressed
render_low_limit = 10000  # automatically starts rendering the game if the agent has survived for this long
render_episode_interval = 500  # rendering every x episode

# #####HYPER-PARAMETERS#####
expr = 0.6
lr = 0.4
agent.set_exploration(expr)
agent.set_learning_rate(lr)
agent.set_discount_rate(0.99)
num_episodes = 20000
max_episode_length = 1000000
exp_decay_denominator = 2000
lr_decay_denominator = 3000

# Setting up the plot
frames_vector = []  # y-coordinates
pos_vector = []  # x-coordinates
plt.ion()
figure = plt.figure()

# Training the agent
for episode in range(num_episodes):
    observation = env.reset()
    action = 0
    curState = -1

    # Upper limit of 1 mill. decisions in each episode
    for t in range(max_episode_length):

        # Rendering the environment if requirements are met
        if t % 100 == 0 and keyboard.is_pressed('a'):
            rendering = not rendering
            time.sleep(0.5)
        elif episode % render_episode_interval == 0 or t == render_low_limit:
            rendering = True
        if rendering and not abort_rendering:
            env.render()

        # execute the action and get new observation, the built in reward and done (if the game is over) is not used,
        # but a custom variant is instead implemented
        observation, _reward, _done, _ = env.step(action)

        # custom done function; the episode is over if it tilts more than 12 degrees or is out of the screen
        done = abs(observation[0]) >= 2.4 or abs(observation[2]) > 12 * math.pi / 180

        # updating current- and previous state
        prev_state = curState
        curState = agent.get_state(observation[0], observation[1], observation[2], observation[3])

        # Update Q_value of previous state_action pair
        if t > 0:
            # Custom reward function that penalizes tilting and distance from center
            reward = -1 if done else 1
            reward -= min(1, abs(observation[2] * 5)) - abs(observation[0] / 2)

            agent.update_q_value(prev_state, action, curState, reward, done)

            # Decreasing exploration- and learning_rate
            agent.set_exploration(max(0, expr - episode / exp_decay_denominator))
            agent.set_learning_rate(max(0.1, lr - episode / lr_decay_denominator))

            # Finding next action
            action = agent.get_action(curState)

            # Game is finished
            if done:
                highest_score = max(highest_score, t)  # longest time alive
                print("Episode finished after {} timesteps".format(t + 1) + " attempt " + str(
                    episode) + " highest_score ",
                      highest_score)
                add_point(t)  # adding point to graph
                rendering = False
                break
