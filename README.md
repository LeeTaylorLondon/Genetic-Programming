# Genetic-Programming Concept

A short explaination of genetic programming:  
You are tasked with improving the design of an electrical circuit board. To achieve this you modify the existing design by adding, 
removing, replacing, and moving components on the circuit board. However, a possibly more efficient way of improving the design
is by simulating the circuit board and generating a population of randomly generated circuit boards. Each population member is made up
of a different combination of components. The efficiency of each board is measured, the best two boards are selected and 
then their components are mixed together to randomly generate a new population of circuit boards.  
This process of selecting the best two population members and randomly mixing their components together is repeated 
until the target efficiency is met or the design can no longer be improved by this process.  
This process is a brief example of genetic programming. 

## Project Brief
#### Node Class
Each node stores a value and might have two children and a parent Node
* Contains pointer to left and right child
* Contains pointer to parent
* Contains value - either a function or integer
#### NodeStructure Class
There are rules for the way a structure of Nodes is formed in order to represent a formuale
* Generate random node function
* Generates a tree of correctly linked Nodes
* Interpreter evaluates the formulae
#### GeneticProgram Class
This is both a container for NodeStructures and where genetic functions are applied to reach a goal
* Stores a list of NodeStructures as a population
* Performs genetic functions crossover, mutation, duplication
* Performs genetic functions until goal is reached
#### GUI Class
This renders the contents of the program for useability and debugging purposes
* Renders a NodeStructureGUI object 
* Used to display the population of the GeneticProgram
* Able to render multiple generations of NodeStructureGUIs

## Project Contents Overview

![Program GUI](https://github.com/LeeTaylorNewcastle/Genetic-Programming/blob/main/imgs/gui.png?raw=true)
