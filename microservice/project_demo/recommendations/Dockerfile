FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
COPY ca.pem /service/recommendations/
WORKDIR /service/recommendations
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations -keyout server.key -out server.csr
RUN --mount=type=secret,id=ca.key openssl x509 -req -in server.csr -CA ca.pem -CAkey /run/secrets/ca.key -set_serial 1 -out server.pem

EXPOSE 443
ENTRYPOINT [ "python", "recommendations.py" ]

