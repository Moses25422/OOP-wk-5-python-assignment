# OOP Assignment: Superheroes and Vehicles

## Overview
This PyGame application demonstrates key Object-Oriented Programming (OOP) concepts through an interactive visualization featuring superheroes and vehicles. 
The program showcases class design, inheritance, and polymorphism in a visually engaging way.

## Learning Objectives
- Understand class design with attributes and methods
- Implement inheritance relationships between classes
- Demonstrate polymorphism through method overriding
- Apply encapsulation principles in practice

## Features
- **4 Unique Superheroes**: Each with special powers and visual design
- **3 Different Vehicles**: Cars, airplanes, and boats with unique movement patterns
- **Interactive Elements**: Press SPACE to see superhero powers in the console
- **Visual Demonstrations**: Clear visualization of OOP concepts

## OOP Concepts Demonstrated

### 1. Class Design (Superhero Class)
- Attributes: name, secret identity, power level, color, position
- Methods: use_power(), draw(), move()
- Constructor initializes each object with unique values

### 2. Inheritance (TechHero extends Superhero)
- Inherits all Superhero properties and methods
- Adds specialized gadget attribute
- Overrides use_power() method for specialized behavior

### 3. Polymorphism (Vehicle Classes)
- Base Vehicle class with abstract move() and draw() methods
- Car, Airplane, and Boat subclasses implement move() differently:
  - Car.move(): "Driving" behavior
  - Airplane.move(): "Flying" behavior  
  - Boat.move(): "Sailing" behavior

## How to Run
1. Ensure Python and PyGame are installed:
   ```
   pip install pygame
   ```
2. Run the Python script
3. Watch the superheroes and vehicles move with their unique behaviors
4. Press SPACE to see superhero powers displayed in the console

## Controls
- **SPACE**: Display superhero powers in console
- **Close Window**: Exit the application

## Technical Implementation
- Built with PyGame for visualization
- Uses Python classes to model superheroes and vehicles
- Implements inheritance through class extension
- Demonstrates polymorphism through method overriding
- Shows encapsulation through class-based data organization

This application serves as both an educational tool for understanding OOP principles and an engaging visual demonstration of how these concepts work in practice.
