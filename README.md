# Kubernetes-Django

To deploy this solution :

git clone https://github.com/Jocor1n/Kubernetes-Django.git

$ docker build -t djangokubernetesproject .

To test before Kubernetes :
$ docker run -p 80:8000 djangokubernetesproject
in a browser : http://127.0.0.1

$ kubectl apply -f django-deployment.yaml
$ kubectl apply -f django-svc.yaml

Test the infrastrustures :

$ kubectl get svc django
$ kubectl get nodes django

