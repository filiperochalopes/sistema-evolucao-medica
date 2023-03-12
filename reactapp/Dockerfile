FROM node:16-alpine as build_stage

RUN mkdir -p /home/node/app

WORKDIR /home/node/app

COPY . .
COPY package.json .
COPY .env .env

ARG PUBLIC_URL
ENV PUBLIC_URL=${PUBLIC_URL}

RUN yarn config set network-timeout 300000
RUN yarn 
RUN yarn build

FROM nginx:1.16.0-alpine

RUN mkdir -p /usr/share/nginx/html/admin
COPY --from=build_stage /home/node/app/build /usr/share/nginx/html/admin
COPY nginx/production.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]