# RPLidarVirtualisation

4.1.4.	Görselleştirme  Yöntemleri
Bu çalışmada verilerin insanlar tarafından daha iyi anlaşılabilmesi, dosya formatının literatürde kullanılan formatta olması ve veriler üzerinde daha iyi filtreleme yapılabilmesi ve karşılaştırılabilmesi amacıyla birden fazla görstelleştirme yöntemleri kullanılmıştır.Verileri görselleştirme için tüm yöntemlerde Python programlama dili kullanılmıştır.

4.1.4.1 Open3D Kütüphanesi 

   Open3D kütüphanesi, üç boyutlu nokta bulutlarının işlenmesi, görüntülenmesi ve analizi için kullanılan açık kaynaklı bir Python kütüphanesidir. Open3D, görüntü işleme ve derin öğrenme uygulamaları için yaygın olarak kullanılan 3D algoritmaları ve işlevler sunar.

  Programlama dilinde Open3D kullanarak Verileri Görselleştirme Aşamaları:


  1. 	Python ve RPLidar bağlantısı için : RPLidar kütüphanesi
  2.	Alınan verilerin Open 3D ile görüntülenmesi için PCD dosyasına çevirme
  3.	PCD dosyasından okunan veriler ile Open3D kütüphanesinin kullanılması

  ![image](https://github.com/cancakmk/RPLidarVirtualisation/assets/44982664/e8ceb45b-33da-4a8e-be02-c00414590f27)



4.1.4.1.1 PCD Dosya Formatı Nedir ?
		PCD (Point Cloud Data) dosya formatı, 3D nokta bulutu verilerini depolamak için kullanılan bir dosya formatıdır. PCD formatı, noktaların 3D koordinatlarını ve isteğe bağlı olarak diğer nokta özniteliklerini içeren verileri tutar. PCD dosyaları genellikle lazer tarama, 3D sensörler veya diğer 3D veri kaynaklarından elde edilen nokta bulutlarını temsil etmek için kullanılır. Her nokta, 3D uzayda X, Y ve Z koordinatlarıyla temsil edilir. Ayrıca, noktalara ekstra renk, yoğunluk veya normal vektörleri gibi öznitelikler eklenebilir. Yapılan çalışmada kullanılan lidardan alınan veriler 2 boyutlu veriler olduğundan Z koordinatı daima 0 olacak şekilde dosyaya yazdırılmıştır.


	
4.1.4.2 PyGame Kütüphanesi 
	Nokta bulutlarının doğru şekilde gözlemlenmesi amacıyla alınan veriler aynı zamanda bir Csv dosyasına kayıt edilmiştir.Elde edilen veriler ile ayrıca PyGame kütüphanesi kullanılarak görselleştirilmesi amaçlanıştır.

Programlama dilinde Pygame kullanarak Verileri Görselleştirme Aşamaları:
		

  1. 	Python ve RPLidar bağlantısı için : RPLidar kütüphanesi
  2.	Alınan verilerin Pygame ile görüntülenmesi için Csv dosyasına çevirme
  3.	Csv dosyasından okunan veriler ile Pygame kütüphanesinin kullanılması

![image](https://github.com/cancakmk/RPLidarVirtualisation/assets/44982664/74b4f93d-8919-4c07-8355-b5a795098a8a)




4.1.4.3 OpenCV Kütüphanesi 

Nokta bulutlarını işlenmesi amacıyla bir kütüphane daha kullanılmaya karar verilmiştir.Kullanılacak kütüphane gerekli algoritmalar ve fonksiyonları içermeli ve görseller üzerinden de çizgi tespiti yapılabilmesi sağlanmalıdır.Bu nedenle seçilen kütüphane bilgisayarlı görü projelerinde kullanılan OpenCv kütüphanesidir.Bu kütüphane sayesinde lidardan alınan her 360 derecelik görüntü bir fotoğraf şeklinde saklanıp her bir çerçevede çizgi tespiti yapmak için oluşturulmuştur.

![image](https://github.com/cancakmk/RPLidarVirtualisation/assets/44982664/7ee8359e-d0e3-4b07-bab2-2206059e5819)
![image](https://github.com/cancakmk/RPLidarVirtualisation/assets/44982664/3ab4ef50-ae29-4879-a912-32740ce75457)
![image](https://github.com/cancakmk/RPLidarVirtualisation/assets/44982664/7567369b-7742-4e75-98cd-fcff5074cf6e)






Opencv kütüphanesi sayesinde oluşturulan her bir frame için çizgi tespiti yapılabilir hale gelmiştir.Örneğin 3. örnekte farklı renklerde görünen çizgilerden 96 adet bulunmaktadır.Fotoğraf için gerekli morfolojik işlemler tamamlanıp yukarıdaki şekillerde gösterilmiştir.

Bu proje Kübra Yazar ile birlikte tamamlanmıştır.Ve Tübitak 2209-A projesi kapsamında geliştirilmiştir.
