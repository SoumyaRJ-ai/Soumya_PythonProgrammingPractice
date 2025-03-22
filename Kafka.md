Kafka - real time data streaming tool

- Open-source platform for real-time data handling – primarily through a data stream-processing engine and a distributed event store – to support low-latency, high-volume data relaying tasks.

- Streaming data is information that is constantly produced by hundreds of data sources, most of which provide records of data concurrently. This continuous inflow of data requires a streaming system that can process it sequentially and progressively. Therefore, Kafka has the following major tasks: posting and subscribing to data streams and processing record dataflows in real-time, while storing them in the order in which they were produced.

- Kafka enables asynchronous data flow between processes, applications, and servers, much like other message broker systems. (Asynchronous means it's a nonblocking architecture i.e. multiple tasks can run simulteniously where as Synchronous is blocking architecture which means that the running of one task is highy dependednt on the completion of another task)

- Before Kafka, data processing was traditionally carried out through recurring batch tasks, where raw data is initially stored and then processed at random intervals.

- Kafka does not monitor user activity or remove messages that have been read. it keeps all messages for a predetermined period and leaves it up to the user to track which messages have been read.

- Each node in a Kafka cluster is referred to as a broker, and the Kafka software operates on one or more servers.

- The broker’s responsibility is to assist producer apps in writing data to topics and consumer applications in reading from topics.

- Kafka utilizes an open-source server called Apache ZooKeeper to manage clusters. To make topics more manageable, they are separated into partitions, and Kafka ensures strong ordering for every partition.

- Applications (also known as producers) send data records (i.e., messages) to a Kafka node (broker), where they are processed by other applications (also known as consumers). Apache gathers readable data from a vast array of data sources and groups it into “topics". For consumers to get fresh communications, they must subscribe to the topic, and once they do so, the messages mentioned earlier will be saved automatically.

- Architecture 
	1. Kafka API Architecture
		a. Producer API - An application may submit a data stream to one or many kafka topics via this Producer API 
		b. Consumer API - This one allows applications to manage the stream of data sent to them and subscribe to one or more topics. 
		c. Streams API - Helps applications, performing the duties of a stream processor. Applications receive an input stream from either one or more topics, processes it, 
		and sends the completed stream to the output topics.
		d. Connector API - Helps linking kafka topics to apps or information systems.
	2. Kafka Cluster Architecture (follow this link later to know more https://www.spiceworks.com/tech/data-management/articles/what-is-kafka/)
		a. Kafka Brokers
		b. Kafka ZooKeepers
		c. Kafka Producers
		d. Kafka Consumers
