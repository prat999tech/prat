<h1 align="center">File Wizard</h1>

<p align="center">
  An open-source file conversion webapp built with ReactJs, Python<br>
  and AWS for the HTTP API, Lambda functions and S3 object storage.<br>Converts .docx files to .pdf
</p>

## Features

- **Website**
  - [ReactJs](https://react.dev/) App Router
  - [Amazon Web Services](https://docs.aws.amazon.com/) for backend functionality
  - Support for `HTTP API`, `S3` File Storage, and `Lambda` functions
  - Edge runtime-ready
  
- **AWS Infrastructure**
  - [Amazon S3](https://aws.amazon.com/s3) Allows for object storage and static site hosting
  - [API Gateway](https://aws.amazon.com/eventbridge) hosts the HTTP API 
  - [AWS Lambda](https://aws.amazon.com/lambda) for processing JSON and filtering required data
  - [Amazon EC2](https://aws.amazon.com/sns) for provisioning VM instances
 
## Overview
![image](https://github.com/sankalpx5/docx-to-pdf-convertor/assets/115892823/613b1f40-d287-4d11-a353-d58f6faf74ae)


A static site is hosted on `S3` with a document upload form. We use `API Gateway` to create an API which makes a `GET` request to a `Lambda` function after the user clicks <kbd>Upload File</kbd> on the form.

The API sends a `presigned bucket URL` for the `uploads-bucket`. The site then automatically conducts a `PUT` request to the same bucket with the `.docx` file data.

Another `Lambda` function is configured to listen for `PUT Object events` in the S3 `uploads-bucket`. It parses the event record for file name and sends a `POST` request to the Python `Flask App` performing the document conversion.

An `EC2` instance is deployed with an Ubuntu OS image. A python script is setup to run as a background process.

The python `microservice` converts documents using `pandoc` package and is exposed as an API using `Flask` listening for `POST` requests on a specified port. It downloads and saves the specified file with its ID, uploads the converted file to the `output-bucket` on `S3` and performs cleanup for files saved during runtime.

The static site returns the download link for the converted file from the `output-bucket`.
