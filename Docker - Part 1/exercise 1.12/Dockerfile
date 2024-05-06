FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

RUN npm install -g serve

EXPOSE 5000

# Command to serve the static files
CMD ["serve", "-s", "-l", "5000", "build"]



