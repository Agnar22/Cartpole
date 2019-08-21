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
I created this project to get insight into the mathematics behind backpropagation in neural networks, 
as well as to learn how to implement it by only using matrix operations. Numpy is used for the matrix operations.

To check if the neural network (both feed forward and backpropagation) was working, I tested it on the MNIST dataset (supplied by tensorflow).

## Results
__coming soon__

## Other resources
* In [this article](https://www.freecodecamp.org/news/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe/ "Diving deeper into Reinforcement Learning with Q-Learning") from freecodecamp, Thomas Simonini explains Q-learning from scratch.
* I also recommend reading [Metthew Chans medium article](https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947 "Cart-Pole Balancing with Q-Learning") on how to solve this problem with Q-learning.
