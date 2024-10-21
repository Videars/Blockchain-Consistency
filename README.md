# Blockchain-Consistency
Master's thesis project with the aim of studying the consistency property of the Sleepy protocol of consensus

## Paper structure:
• Chapter 2: Blockchain and consensus protocols foundations
This chapter introduces the key concepts of blockchains and consensus protocols. It begins with a definition of the blockchain concept and its principal features, followed by a review of the state of the art of some modern consensus algorithms.

• Chapter 3: Sleepy model of consensus
In this chapter, the Sleepy consensus protocol is formally defined, highlighting its operational principles. We described the protocol’s behaviour under static corruptions, providing the necessary elements to understand the analysis we made.

• Chapter 4: Consistency property and proof methods
This chapter reviews the consistency property of the Sleepy protocol. It begins with a formal definition of the consistency property, followed by a review of the current conditions that ensure Sleepy’s consistency. The chapter also introduces the two main proof methods: the classical random variables method and the new proof approach using Markov chains.

• Chapter 5: Markov method application
In this chapter, we applied the Markov chain proof technique to the Sleepy protocol. The chapter illustrates how convergence opportunities are computed, and it presents the results of the analysis, showing the protocol’s increased resistance to adversarial power.

• Chapter 6: Sleepy best attack analysis
Finally we modelled and analyzed the most effective attack on the Sleepy protocol. The chapter begins by showing the adversary’s capabilities and describing the attack model. We provided a pseudocode for the attack to clearly outline the adversary’s steps, enabling an unbiased analysis without the influence of any specific programming language. Then it follows the construction of a Markov chain model to evaluate the probability of success of the attack. The chapter concludes with a solution of the related equations and an analysis of the attack’s impact on the protocol’s ability to reach consensus.
