# CounterChain

Counterchain is a groundbreaking blockchain solution developed on the robust multichain framework, designed to combat the pervasive issue of counterfeit drugs within the supply chain. The project has been extensively researched and validated, and the findings have been published in a research paper with the DOI: 10.1109/ICAC347590.2019.9036794.

This blockchain network operates by enlisting all entities involved in the supply chain, such as manufacturers, distributors, and retailers, as registered nodes. Each entity's machine is connected to the blockchain, ensuring their active participation.

At any given moment, the blockchain records and tracks the presence of every drug within the supply chain. To facilitate seamless interaction with the blockchain, Python PyQT5-powered desktop applications have been meticulously crafted for manufacturers, distributors, and retailers. These applications enable these stakeholders to register new drugs, record transactions, and query the blockchain to validate the authenticity of drugs.

The lifecycle of a drug on the blockchain begins with the manufacturer registering it. As the drug progresses through the supply chain, each transaction involving its ownership change is meticulously documented on the blockchain. As a result, the blockchain consistently maintains an up-to-date record of drug ownership. Any attempt to introduce counterfeit drugs into the supply chain is promptly detected by the system, ensuring heightened security and accountability.

To manage the core functionalities and node registration, an admin node is hosted on AWS EC2. This admin node oversees the onboarding of new entities into the supply chain network as blockchain nodes. The AWS EC2 service delivers robust and scalable performance to meet the demands of the blockchain infrastructure.

To provide the end-users with the ability to verify drug authenticity, a user-friendly mobile application has been skillfully developed. End-users can simply scan the barcode on a drug using the mobile app to confirm its legitimacy. The mobile app communicates with the blockchain to retrieve pertinent information. Due to the resource-intensive nature of querying the blockchain, AWS EC2 and AWS Lambda collaborate to efficiently offload the processing for the mobile application through a socket connection. This setup ensures a smooth user experience without compromising performance or security.

In conclusion, Counterchain stands as a powerful and secure blockchain system, bolstered by the multichain framework and extensively validated through research. The published research paper with DOI: 10.1109/ICAC347590.2019.9036794 supports the efficacy and innovation of this solution. Through its network of registered nodes, desktop applications, and mobile verification, Counterchain ensures transparency, traceability, and real-time detection of any counterfeit attempts, safeguarding the integrity of the pharmaceutical supply chain.
