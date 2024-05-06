FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

COPY . .

EXPOSE 5000

ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN npm install

RUN npm run build

RUN npm install -g serve


# Command to serve the static files
CMD ["serve", "-s", "-l", "5000", "build"]


