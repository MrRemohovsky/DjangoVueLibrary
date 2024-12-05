FROM node:18-slim

WORKDIR /app/frontend/locallibrary

COPY frontend/locallibrary/package*.json ./

RUN npm install

COPY frontend/locallibrary/ ./

EXPOSE 8080

CMD ["npm", "run", "serve"]
