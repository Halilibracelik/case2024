# CASE 2024

Bu proje, Python 3.9 tabanlı bir uygulama çalıştıran bir Docker imajı kullanır.
İçindekiler

    Gerekli Komponentler
    Docker İmajı Oluşturma
    Uygulamayı Çalıştırma
    Katkıda Bulunma

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



### 1. EC2 Makinesi Oluşturma 

    AWS Management Console'a giriş yapın.
    EC2 Dashboard'a giderek Launch Instance butonuna tıklayın.
    Aşağıdaki seçenekleri kullanarak yeni bir EC2 makinesi oluşturun:
        Name: case
        AMI: Ubuntu 20.04 LTS (Amazon Machine Image)
        Instance Type: t3.micro
        Network Settings: Varsayılan ayarları kullanın, ancak SSH (port 22) ve HTTP/HTTPS (port 80/443) erişimlerini güvenlik grubu üzerinden açın.
    Son olarak, Launch Instance butonuna tıklayın ve makineyi başlatın.

### 2. EC2 Makinesine Minikube Kurulumu

EC2 makinesi başlatıldıktan sonra, AWS Systems Manager'ı kullanarak Minikube'u yükleyin:

    AWS Systems Manager bölümüne gidip Session Manager'ı açın.

    EC2 makinesi için bir oturum başlatın.

    Oturum üzerinden aşağıdaki adımları izleyerek Minikube'u kurun:

Minikube ve Kubectl Kurulumu:

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

### 3. Minikube'u Başlatın

Docker sürücüsüyle Minikube'u başlatın:
```
minikube start 
```
### 4. Minikube'un Durumunu Kontrol Edin
Minikube'un durumunu kontrol etmek için:
```
minikube status
```
Ardından, Kubernetes pode'larını kontrol edin:
```
kubectl get nodes
```
Bu komutlar, Minikube'un başarılı bir şekilde çalıştığını doğruladı.

### Sonuç

AWS EC2 üzerinde Minikube kurulumunu tamamen AWS Management Console ve Systems Manager kullanarak gerçekleştirilir. Bu adımlar sonucunda, AWS üzerinde bir Kubernetes ortamı oluşturarak uygulamalarınızı test edebilir ve geliştirebilirsiniz.

### 5. Manifest.yaml'ın Minikube'e Deploy Edilmesi

Manifest dosyası Minikube'e deploy etmek için:
```
Kubectl apply -f manifest.yaml
```

Deployment bölümü, bir Deployment tanımlar. Deployment, Kubernetes üzerinde belirli bir sayıda pod'un çalışmasını sağlar.

Service bölümü, bir Service tanımlar. Service, Kubernetes'te pod'lara ağ üzerinden erişim sağlar.

İngress bölümü, bir Ingress tanımlar. Ingress, HTTP ve HTTPS trafiğini Kubernetes servislerine yönlendirmek için kullanılır.

### Sonuç

Bu manifest.yaml dosyasını Kubernetes kümenize deploy ettiğinizde:

bcfm-case adlı bir pod oluşturulur ve bu pod, halil5841/task_flask:latest image'ını kullanarak çalıştırılır.

Bu pod, küme içinde ve dışında bcfm-case-service adlı bir NodePort servisi aracılığıyla erişilebilir hale gelir. Dış dünyadan bu servise ```http://<NodeIP>:30001``` adresi üzerinden erişilebilir.

bcfm-case.local alan adı üzerinden gelen HTTP trafiği, Ingress aracılığıyla bcfm-case-service servisine yönlendirilir ve bu servis, trafiği pod'a iletir.

### 6. Nginx Servisini Başlatma

nginx.conf dosyası, NGINX'in yerel olarak (localhost) dinlediği 80 numaralı port üzerinden gelen tüm HTTP isteklerini Minikube üzerinde çalışan bir Kubernetes servisine yönlendirmesini sağlar. Minikube servisi ise 192.168.49.2 IP adresi ve 30001 portu üzerinden erişilebilir durumdadır.

Nginx servisini başaltmak için bu komutu çalıştırabilirsiniz.
```
sudo systemctl start nginx
```

