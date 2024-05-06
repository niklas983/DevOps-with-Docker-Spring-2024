# Java 8 from amazoncorretto
FROM amazoncorretto:8

EXPOSE 8080

WORKDIR /usr/src/app


# Copy the Maven files and pom.xml
COPY mvnw .
COPY mvnw.cmd .
COPY pom.xml .

# Copy the source code
COPY . .


# Build the project
RUN ./mvnw package

# Command to run the app
CMD ["java", "-jar", "./target/docker-example-1.1.3.jar"]



