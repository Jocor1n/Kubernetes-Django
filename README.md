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

$ kubectl get svc django --> to see the listening port

Example of Output :
NAME     TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
django   NodePort   10.98.234.155   <none>        8000:31937/TCP   4h53m

$ kubectl get nodes -o wide --> To see what is INTERNAL-IP is

Example of Output :

NAME       STATUS   ROLES           AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE       KERNEL-VERSION    CONTAINER-RUNTIME
minikube   Ready    control-plane   11h   v1.25.3   192.168.49.2   <none>        Ubuntu 20.04.5 LTS   5.10.0-20-amd64   docker://20.10.20

So in a browser, we have to type http://192.168.49.2:31937

