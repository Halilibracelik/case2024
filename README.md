# CASE 2024

### Gerekli Komponentler

Bu projeyi çalıştırmak için aşağıdaki araçlara ihtiyacınız olacak:

    Docker
    Python 3.9

### Docker İmajı Oluşturma ve Çalıştırma

Docker imajını oluşturmak için, proje dizininde aşağıdaki komutu çalıştırın:

```
docker build -t case-study . 
```

Bu komut, bulunduğunuz dizinde yer alan Dockerfile'ı kullanarak case-study isimli bir Docker imajı oluşturur.
Uygulamayı Çalıştırma

Oluşturulan Docker imajını çalıştırmak için aşağıdaki komutu kullanabilirsiniz:


```
docker run -d -p 5000:5000 study-case
```

Bu komut, Docker imajını arka planda (-d bayrağı) 5000 numaralı port üzerinden çalıştırır. Uygulamanıza http://localhost:5000 adresinden erişebilirsiniz.


### GET Request Çıktıları (/ ve /health path'leri için)

![image](https://github.com/user-attachments/assets/16ea7098-0880-4a3b-8b7d-c7e62c1b73f8)                    ![image](https://github.com/user-attachments/assets/5d98de14-db03-40f5-b125-0669463a14dc)

### POST Request Çıktısı

![image](https://github.com/user-attachments/assets/da42413f-3080-408c-ac5c-3696b5425b94)

### Docker İmajının Docker Hub'a Pushlanması

Docker imajını Docker Hub'a pushlamak için, Docker Hub'da oluşturulan reponun bilgileri ile imaj taglanmelidir. Sonrasında Docker Hub'a pushlanabilir.

```
docker tag halil5841/task_flask:latest case-study:latest .

docker push halil5841/task_flask:latest
```

### AWS EC2 Üzerinde Minikube Kurulumu

Bu adım , AWS EC2 üzerinde t3.micro tipinde bir makine kurarak, bu makineye Minikube'u nasıl kurulduğu anlatmaktadır.

### EC2 Makinesi Oluşturma 

AWS Console üzerinde EC2 servisine gidilerek burada launch instance kısmından sanal makine oluşturulur. Security group kısmında 22 portu açılır. Pem dosyası ile ssh yapılarak makineye erişilir.

### EC2 Makinesine Minikube Kurulumu

Minikube ve Kubectl Kurulumu:

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

### Minikube'u Başlatın

Docker sürücüsüyle Minikube'u başlatın:
```
minikube start 
```
Minikube'un durumunu kontrol etmek için:
```
minikube status
```
Ardından, Kubernetes pod'larını kontrol edin:
```
kubectl get pods
```
Bu komutlar, Minikube'un başarılı bir şekilde çalıştığını doğruladı.


### Manifest.yaml'ın Minikube'e Deploy Edilmesi

Manifest dosyası Minikube'e deploy etmek için:
```
Kubectl apply -f manifest.yaml
```

Deployment bölümü, bir Deployment tanımlar. Deployment, Kubernetes üzerinde belirli bir sayıda pod'un çalışmasını sağlar.

Service bölümü, bir Service tanımlar. Service, Kubernetes'te pod'lara ağ üzerinden erişim sağlar.

Bu manifest.yaml dosyasını Kubernetes clustera deploy ettiğinizde:

case adlı bir pod oluşturulur ve bu pod, halil5841/task_flask:latest image'ını kullanarak çalıştırılır.

Bu pod, cluster içinde ve dışında case-service adlı bir NodePort servisi aracılığıyla erişilebilir hale gelir. Dış dünyadan bu servise ```http://<NodeIP>:30001``` adresi üzerinden erişilebilir.


### Nginx Servisini Başlatma

nginx.conf dosyası, NGINX'in yerel olarak (localhost) dinlediği 80 numaralı port üzerinden gelen tüm HTTP isteklerini Minikube üzerinde çalışan uygulamanın servisine yönlendirmesini sağlar. Uygulama servisi ise 192.168.49.2 IP adresi ve 30001 portu üzerinden erişilebilir durumdadır.

Nginx servisini başaltmak için bu komutu çalıştırabilirsiniz.
```
sudo systemctl start nginx
```

### LoadBalancer Oluşturulması

AWS üzerinde EC2'nun önüne LoadBalancer konumlandırılmıştır. Bu işlem için AWS Console üzerinde EC2 servisinin altında Load Balancers kısmında Create LoadBalancer seçeneği ile oluşturulmuştur. Bu kısımda application loadbalancer seçilmiştir. Loadbalancer, uygulamanın çalıştığı ec2 ile aynı networkde olacak şekilde ayarlanmıştır. Loadbalancer'ın istekleri uygulamaya iletebilmesi için target group oluşturularak EC2 makine target group'a register edilmiştir. 

![image](https://github.com/user-attachments/assets/d6a45681-4036-4018-8e9d-c0a3ac78ff65)


![image](https://github.com/user-attachments/assets/92999117-2e64-46b2-b8ec-9fbbf237571d)


### Case Çıktıları

- Case'de istenilen API uygulaması geliştirilerek Containerize edilmiştir.
- Oluşturulan image Docker Hub'a gönderilmiştir. 
- AWS üzerinde bir EC2 makine oluşturularak bu makine içerisine minikube kurulumu yapılmıştır. 
- Uygulamayı kubernetes üzerine deploy etmek için manifest dosyaları oluşturulmuştur. 
- Manifest dosyasının içinde deployment ve service tanımları bulunmaktadır. Service tanımı nodeport olarak yapılmıştır. 
- Bu sayede uygulama dışardan erişim için uygun hale getirilmiştir. 
- EC2 makine içerisine nginx kurulumu yapılarak makineye 80 portundan gelecek istekleri service nodeport'una yönlendirecek nginx konfigürasyonu yapılmıştır. 
- AWS üzerinde oluşturulan loadbalancer'a target olarak bu EC2 makinesi verilmiştir. 
- Loadbalancer 80 portundan gelen istekleri alarak EC2 makinesine göndermekte ve makine içerisinde nginx bu isteği alarak uygulamaya iletmektedir.

LoadBalancer DNS:

http://case2024-alb-1960691765.eu-north-1.elb.amazonaws.com/

http://case2024-alb-1960691765.eu-north-1.elb.amazonaws.com/health
