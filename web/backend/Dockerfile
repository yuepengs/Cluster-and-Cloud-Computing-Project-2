FROM node:16.5.0
ENV PATH /app/node_modules/.bin:$PATH
WORKDIR /app
COPY package*.json ./
RUN npm ci --silent
COPY . .
EXPOSE 8000
CMD ["npm","start"]
