# Human Interaction with Computer Vision

## Overview

This project is developed for the course of "Human-Computer Interaction" and focuses on integrating computer vision into interactive applications. Specifically, it implements the classic game of Rock-Paper-Scissors using computer vision.

## Summary

The project enables users to play Rock-Paper-Scissors by leveraging computer vision to recognize hand gestures captured via a camera. The process is as follows:

- The user performs a hand gesture (rock, paper, or scissors) in front of the computer camera.
- The program recognizes the gesture using computer vision techniques.
- The computer then selects a move arbitrarily.
- The program displays the computer’s move and determines the outcome (win, lose, or draw).

This implementation is based on the demonstration provided in the following YouTube video: [Rock-Paper-Scissor using Computer Vision](https://www.youtube.com/watch?v=k2EahPgl0ho).

## Installation Instructions

To run this project, ensure you have the following:

1. **Python Version**: A 64-bit version of Python 3.9 or higher.
2. **Required Libraries**:
   - `mediapipe==0.10.13`
   - `cvzone`

Install the required libraries using pip:

pip install mediapipe==0.10.13 cvzone
