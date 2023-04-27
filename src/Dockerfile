# syntax=docker/dockerfile:1

FROM node:18-alpine
WORKDIR /src
COPY . .
RUN yarn install --production
EXPOSE 8000