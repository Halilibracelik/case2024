# case2024
Case Study

Bu proje, Python 3.9 tabanlı bir uygulama çalıştıran bir Docker imajı kullanır.
İçindekiler

    Kurulum
    Docker İmajı Oluşturma
    Uygulamayı Çalıştırma
    Katkıda Bulunma

Kurulum

Bu projeyi çalıştırmak için aşağıdaki araçlara ihtiyacınız olacak:

    Docker yüklü olmalıdır.
    Python 3.9 (eğer Docker kullanmadan çalıştırmayı planlıyorsanız)

Docker İmajı Oluşturma

Docker imajını oluşturmak için, proje dizininde aşağıdaki komutu çalıştırın:

bash

docker build -t case-study .

Bu komut, bulunduğunuz dizinde yer alan Dockerfile'ı kullanarak case-study isimli bir Docker imajı oluşturur.
Uygulamayı Çalıştırma

Oluşturulan Docker imajını çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

bash

docker run -d -p 5000:5000 study-case

Bu komut, Docker imajını arka planda (-d bayrağı) 5000 numaralı port üzerinden çalıştırır. Uygulamanıza http://localhost:5000 adresinden erişebilirsiniz.
