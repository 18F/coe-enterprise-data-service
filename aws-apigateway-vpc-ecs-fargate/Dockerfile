FROM node:16
WORKDIR /usr/src/app
COPY "package*.json" "./"
RUN npm cache clean --force
RUN npm install 
COPY . .
EXPOSE 80
CMD ["npm","start"]
