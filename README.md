# Cartpole

Reinforcement learning solution to the [Cartpole environment](http://gym.openai.com/envs/CartPole-v1/ "Cartpole_v1") from OpenAI gym.

This agent uses a Q-learning approach to learn how to balance the pole by moving the cart, given the horizontal position- and velocity of the cart in addition to the angle- and angle velocity of the pole.

## Installation
Clone the repository
```bash
git clone https://github.com/Agnar22/Cartpole.git
```

navigate into the project folder
```bash
cd Cartpole
```

install requirements
```bash
pip install -r requirements.txt
```

if everything went well, you should now be able to run the code
```bash
python3 Main.py
```

## Motivation
This project served several purposes. I wanted to try out the entry level RL problem from OpenAI gym, Cartpole, as well as learn how to implement the suggested solution. Being familiar with Q-learning also has other advantages due to the applicability of this algorithm in the RL world.

## Results
<p align='center'>
<img align='middle' width="40%" src="https://github.com/Agnar22/Cartpole/blob/master/training.gif">
</p>
The problem is easily solvable with q-learning, as demonstrated above. It needed about 3000 episodes to reach the final fitness where it __perfectly__ balances the pole in the middle of the screen.

## Other resources
* In [this article](https://www.freecodecamp.org/news/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe/ "Diving deeper into Reinforcement Learning with Q-Learning") from freecodecamp, Thomas Simonini explains Q-learning from scratch.
* I also recommend reading [Metthew Chans medium article](https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947 "Cart-Pole Balancing with Q-Learning") on how to solve this problem with Q-learning.
