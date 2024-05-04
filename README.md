# Bank System

## Overview

Bank System is a comprehensive banking solution that integrates various features including a loan chatbot, insurance claim chatbot, credit score assessment, and transaction monitoring with fraud detection. This project aims to provide a seamless banking experience for users by leveraging advanced technologies such as language models, convolutional neural networks (CNN), and SQL database integration.

## Features

### Loan Chatbot

The loan chatbot assists users in exploring loan options, providing information about interest rates, loan terms, and eligibility criteria. It utilizes Langchain integration to facilitate natural language understanding and responses.

### Insurance Claim Chatbot

The insurance claim chatbot streamlines the process of filing insurance claims. It employs a CNN model to detect damages, which are then cross-referenced with user insurance data stored in an SQL database. The chatbot informs users whether their insurance covers the claimed damages or not.
![alt text](<Untitled Diagram.drawio (1).png>)


### Credit Score Assessment

Bank System evaluates the credit score of each customer based on their financial data. This assessment helps in determining the creditworthiness of users and guides decision-making processes related to loan approvals and interest rates.

### Transaction Monitoring with Fraud Detection

Transactions made through Bank System are monitored in real-time using a fraud detection model. This model analyzes transaction patterns and flags suspicious activities. Users are promptly alerted if a transaction is deemed potentially fraudulent, ensuring the security of their accounts.

## Technologies Used

- Langchain for natural language processing in chatbots
- Convolutional Neural Networks (CNN) for damage detection in insurance claims
- SQL database for storing user information and insurance data
- Fraud detection model for real-time transaction monitoring
- PDF source integration for document management

## Usage

1. Clone the repository: `git clone https://github.com/yourusername/bank-system.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python multipage.py`
4. Access the Bank System through your web browser.



