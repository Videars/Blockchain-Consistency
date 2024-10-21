# Blockchain-Consistency
**Master's thesis project**  
*Consistency of the Sleepy protocol of consensus with Markov chains.*

## Paper Structure

### Chapter 2: Blockchain and Consensus Protocols Foundations
This chapter introduces the key concepts of blockchains and consensus protocols. It covers:
- A definition of the **blockchain** concept and its main features.
- A review of the state of the art of modern **consensus algorithms**.

### Chapter 3: Sleepy Model of Consensus
In this chapter, the **Sleepy consensus protocol** is formally defined. Key elements include:
- **Operational principles** of the Sleepy protocol.
- The protocol’s behavior under **static corruptions**, providing the necessary elements for further analysis.

### Chapter 4: Consistency Property and Proof Methods
This chapter focuses on the **consistency property** of the Sleepy protocol. It includes:
- A formal definition of the **consistency property**.
- A review of the **current conditions** that ensure Sleepy’s consistency.
- An introduction to two main **proof methods**:
  - The classical random variables method.
  - A new proof approach using **Markov chains**.

### Chapter 5: Markov Method Application
In this chapter, the **Markov chain proof technique** is applied to the Sleepy protocol. It covers:
- Computation of **convergence opportunities**.
- Results of the analysis showing the protocol’s increased **resistance to adversarial power**.

### Chapter 6: Sleepy Best Attack Analysis
This chapter models and analyzes the **most effective attack** on the Sleepy protocol. It includes:
- **Adversary capabilities** and description of the attack model.
- Pseudocode of the attack, outlining the steps of the adversary.
- A **Markov chain model** to evaluate the probability of success of the attack.
- A solution to the related equations, along with an analysis of the **attack’s impact** on the protocol’s ability to reach consensus.
