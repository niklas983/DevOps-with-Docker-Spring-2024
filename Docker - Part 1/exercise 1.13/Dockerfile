FROM golang:1.16-alpine

WORKDIR /usr/src/app

COPY . .

EXPOSE 8080

# environment variables
ENV REQUEST_ORIGIN=http://localhost:5000  

RUN go build

# execute app
CMD ["./server"]

