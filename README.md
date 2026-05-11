````markdown
# CCS 2226 Foundations of Artificial Intelligence — Practical Tasks & CAT

## Student Information

**Name:** Osoro Daniel Kinara
**Reg No:** CIT-227-080/2024
**Course:** BSc Software Engineering  
**Unit:** CCS 2226 Foundations of Artificial Intelligence  

# Project Overview

This repository contains solutions for:

1. Practical Tasks
2. CAT Task

The project demonstrates fundamental Artificial Intelligence concepts including:

- Machine Learning
- Constraint Satisfaction Problems
- Logic Programming
- Search Algorithms
- Intelligent Agents

# Technologies Used

- Python 3.14.3
- pip 3.14
- SWI-Prolog
- PyTorch
- python-constraint library

# Project Structure

```text
Foundations_Of_AI
│
├── Task1
│   └── main.py
│
├── Task2
│   ├── australia.py
│   └── nairobi.py
│
├── Task3
│   └──
│
├── Task4
│   ├──
│   └──
│
├── CAT1
│   ├── question1-b.py
│   └── vacuum_agent.py
│
└── README.md
```
````

# PRACTICAL TASKS

# TASK 1 — MNIST Dataset

## Objective

To download and use the MNIST dataset for handwritten digit recognition using Artificial Intelligence.

## Features

- Downloads MNIST dataset
- Loads image data
- Trains a neural network
- Classifies digits 0–9
- Tests model accuracy

## Libraries Used

```bash
pip install torch torchvision matplotlib numpy
```

## Running the Program

```bash
python main.py
```

## Expected Output

```text
Training completed!
Accuracy: 95%
```

# AI Concepts Demonstrated

- Machine Learning
- Neural Networks
- Image Classification
- Deep Learning Basics

# TASK 2 — Constraint Satisfaction Problem (CSP)

## Australia Map Colouring

The program colours Australian regions using:

- Red
- Green
- Blue

Constraint:

- Adjacent regions cannot share the same colour.

## Nairobi Sub-County Colouring

The program colours the 17 sub-counties of Nairobi using the least number of colours while ensuring neighbouring sub-counties do not share colours.

## Library Installation

```bash
pip install python-constraint
```

## Running CSP Programs

```bash
python australia.py
```

```bash
python nairobi.py
```

# AI Concepts Demonstrated

- Constraint Satisfaction Problems
- Graph Colouring
- Search Algorithms
- Problem Solving

# TASK 3 AND TASK 4 COMING SOON!

# CAT TASK

# QUESTION 1 — A\* Search Algorithm

## Objective

Implement the A\* Search Strategy to optimize path resources.

## Formula Used

f(n) = g(n) + h(n)

Where:

- g(n) = actual path cost
- h(n) = heuristic estimate
- f(n) = total estimated cost

## Running the Program

```bash
python question1-b.py
```

# AI Concepts Demonstrated

- Heuristic Search
- Optimal Pathfinding
- Resource Optimization

# QUESTION 2 — Vacuum Cleaner Agent

## Objective

Design a simple intelligent vacuum cleaner agent.

## Features

- Detects dirty rooms
- Cleans automatically
- Changes room states

## Running the Program

```bash
python vacuum_agent.py
```

# AI Concepts Demonstrated

- Intelligent Agents
- Environment Interaction
- Automated Decision Making

# PEAS AND PAGE

The CAT also includes analysis of:

- PEAS
- PAGE

for an Automatic DNA and Genomic Sequencing System.

# How to Run All Programs

## Python Programs

Example:

```bash
python filename.py
```

## Prolog Programs

Start SWI-Prolog:

```bash
swipl
```

Load program:

```prolog
['family.pl'].
```

# Installation Guide

## Install Python Libraries

```bash
pip install torch torchvision matplotlib numpy python-constraint
```

# Learning Outcomes

Through this project, the following AI skills were demonstrated:

- Machine Learning
- Constraint Satisfaction
- Logic Programming
- Intelligent Agents
- Heuristic Search
- Graph Traversal
- AI Problem Solving

# GitHub Submission

Push all files to GitHub and submit repository link as instructed by the lecturer.

# Author

Name:Osoro Daniel Kinara.

RegNo:CIT-227-080/2024.
