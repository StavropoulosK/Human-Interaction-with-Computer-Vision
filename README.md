# Human Interaction with Computer Vision

## Overview

This project is developed for the course of "Human-Computer Interaction" for the academic year 2024-25 and focuses on integrating computer vision into interactive applications. Specifically, it implements the classic game of Rock-Paper-Scissor using computer vision.

## Summary

The project enables users to play Rock-Paper-Scissor by leveraging computer vision to recognize hand gestures captured via a camera. The process is as follows:

- The user performs a hand gesture (rock, paper, or scissor) in front of the computer camera.
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
3. **Project Structure:** Ensure the folder Resources is located in the same directory as app.py.

Install the required libraries using pip:

pip install mediapipe==0.10.13 cvzone

Also, you need to have the folder Resources within the same folder as app.py
