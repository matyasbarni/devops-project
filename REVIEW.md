# Top 5 most important things to fix

After examining the project I have some recommendations in order for it to function properly:

- 1.: The deployment and service inside the helm templates folder are using different selectors and names, the service app selector has to point to a valid app name.
- 2.: The chart path is invalid in the terraform code, it should point to the root directory of helm.
- 3.: The service target port does not match the container port, they have to be the same in order for them to be able to communicate.
- 4.: Please also correct the service name reference inside the ingress, they are also mismatched.
- 5.: The value of image.tag in the terraform helm release set block is missing, please provide a valid value for it.
- +1.: Please pay attention to formatting the code correctly, it makes it easier to read and maintain. You can use plugins for that, but a simple terraform fmt can make a day and night difference also!