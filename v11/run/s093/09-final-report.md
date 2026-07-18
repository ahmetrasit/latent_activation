# S93:1–11 (ed-Duhâ) — Nihai Bütünleştirme Raporu

## Kapsam ve yöntem notu

Bu rapor, S93:1–11 için `00-surah-text.json`, `01-passage.json`, `02-branches.json`, `03-candidate-bridges.json`, `05-activation-pass.json`, `06-mechanism.md`, `07-secondary-expansion.json`, `08-graph.json` ve mekanik keşif kuyruğu olan `10-discovery-ranking.json` dosyalarını bütünleştirir. QAC kelime sırası, morfoloji ve kök çözümlemesinde; `00-surah-text.json` ise tilavet metninde esas alınmıştır. Besmele analiz çerçevesine dahildir; ancak sağlanan branch envanteri 1. ayetle başladığından Besmele’ye mahsus yeni kök veya branch kimliği üretilmemiştir. Kök çözümlemesinde 23 kökün tamamı çözülmüş, eksik ya da dışarıda bırakılmış kök bulunmamıştır.

> بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ  
> وَٱلضُّحَىٰ  
> وَٱلَّيْلِ إِذَا سَجَىٰ  
> مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ  
> وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ  
> وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ  
> أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ  
> وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ  
> وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ  
> فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ  
> وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ  
> وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ

## Kısa nihai rapor

Sûrenin birincil mekanizması **teselli → hatırlatılmış kanıt → etik aktarım** çizgisidir. Kuşluk aydınlığı ile çöken gecenin dinginliği yan yana getirilir (`ض ح و B001`; `ل ي ل B001`; `س ج و B001`). Bu karşıtlık, görünürlüğün azalmasını ilahî ilişkinin kesilmesi saymayı engeller. Ardından korkunun iki biçimi doğrudan reddedilir: Rab ne terk etmiş ne de nefret etmiştir (`و د ع B001`; `ر ب ب B001`; `ق ل ي B003`). Böylece sessizlik, vedaya değil devam eden bakıma ait bir evre olarak okunur.

Teselli yalnız şimdiki korkuyu gidermekle kalmaz; zamanı daha iyi bir ufka açar. Sonraki/âhiret, ilk evreden daha hayırlıdır (`ء خ ر B004`; `خ ي ر B001`; `ء و ل B001`) ve Rabbin vereceği şey rızaya ulaştıracaktır (`ع ط و B002`; `ر ض و B001`). Buradaki “daha iyi”, salt nicelik artışı değil; hayır, seçkin değer, doğru tercihi ayırt etme, ihsan ve ilişkinin onarılmış tatminiyle genişleyen bir sonuçtur (`خ ي ر B002/B003/B005`; `ر ض و B002/B004`).

Gelecek vaadinin delili, geçmişte üç kez işleyen uygun karşılık örüntüsüdür. `وَجَدَكَ` tekrarı (`و ج د B001`), her kırılganlığı ona uygun bir bakımla eşler: yetimlik barınmayla (`ي ت م B001`; `ء و ي B001`), yönsüzlük hidayetle (`ض ل ل B001`; `ه د ي B001`), maddî yoksunluk ise yeterlilikle (`ع ي ل B001`; `غ ن ي B001`) karşılanır. “Bulma”, ilahî bilgisizlikten sonra tesadüfî keşif değil; durumu gören, tanıyan ve gereken karşılığı sağlayan dikkatli mevcudiyet işlevindedir (`و ج د B002/B003/B004`).

Son üç emir, geçmişte alınan bakımın toplumsal dolaşıma sokulmasıdır. Barındırılmış olan, yetimi ezmemelidir (`ي ت م B001/B002`; `ق ه ر B001`); ihtiyacı giderilmiş olan, isteyeni sertçe kovmamalıdır (`س ء ل B001`; `ن ه ر B004`); Rabbin nimetini alan ise onu doğru biçimde anlatmalıdır (`ن ع م B001`; `ح د ث B003`). Dolayısıyla sûrenin sonu teselliye eklenmiş bağımsız ahlâk hükümleri değildir: alınmış barınak, hidayet ve yeterlilik; koruma, açık iletişim ve şükür tanıklığı olarak başkasına geçer.

Besmelenin rahmet çerçevesi bu dolaşımın yönünü belirler. Rahmet Rabden muhataba; oradan yetime, isteyene ve kamusal söze geçer. Sûrenin bütüncül iddiası şudur: görünmeyen bakım terk ediliş değildir; geçmişte uygun karşılıklar üretmiş Rabbanî bakım geleceğe de uzanır ve kendisine bakım ulaşan kişiyi, başkasının kırılganlığı karşısında aynı bakım mantığının taşıyıcısı yapar.

### Yorum sınırları

- `A`, yüzey ve bağlam tarafından doğrudan taşınan okumadır; `B`, bağlamca güçlü ikincil aktivasyondur; `C/B`, kontrollü fakat ihtiyatlı latent okumadır; `C`, keşif rezervuarında korunup yerel mekanizmaya alınmayan okumadır.
- İkincil okumalar yüzey anlamını değiştirmez: örneğin `وَدَّعَكَ` yüzeyde “emanet etti”ye, `سَجَىٰ` “yağmur yağdırdı”ya, `تَنْهَرْ` “bulut”a çevrilmez. Bu dallar yalnız ilişkinin ve bakımın altında çalışan kavramsal modeli genişletir.
- `10-discovery-ranking.json` bir yorum hükmü değil, muhtemel sürpriz değerine göre mekanik inceleme kuyruğudur. Yüksek puanlı ama yerel denetimi zayıf kümeler aşağıda `C` olarak korunmuştur.

## Aktive edilmiş branch tablosu

Envanter muhasebesi: **23 kök, 167 branch; A=23, B=55, C/B=29, C=60; kapsam=complete; S=0, X=0.** Aşağıdaki tablo seçici değildir; aktivasyon geçişindeki bütün branch rezervuarını korur.

| Kök | Branch’ler ve aktivasyon rolleri |
|---|---|
| ض ح و | `B001 [A]` kuşluk aydınlığı ve teselli çerçevesi; `B002 [B]` görünür ışığa çıkış; `B003 [C/B]` gündüz beslenmesi ve rızık; `B004 [C]` kurban ve ibadet alt-katmanı; `B005 [B]` çöken geceye karşı berrak parlaklık; `B006 [B]` yumuşaklık, sabır ve merhametli sakınma. |
| ل ي ل | `B001 [A]` karanlık ve kozmik karşı kutup olarak gece; `B002 [C]` gece faaliyeti ve yolculuk; `B003 [C/B]` düzenli zaman ardışıklığı içindeki gece; `B004 [C]` Leyla adı ve kültürel mecaz. |
| س ج و | `B001 [A]` gecenin dinginliğe çökmesi; `B002 [C/B]` koruyucu örtme ve bürünme; `B003 [C/B]` yerleşik ahlâkî yatkınlık; `B004 [B]` zarar verici temastan sakınma; `B005 [B]` gözetim ve süreğen bakım; `B006 [B]` bol ve hayatı sürdüren rızık. |
| و د ع | `B001 [A]` açıkça reddedilen terk; `B002 [B]` süren bakım altındaki güvenli dinlenme; `B003 [B]` reddedilen veda ve keder; `B004 [C/B]` karşılıklı saldırmazlıkla barış; `B005 [B]` terk yerine emanet edilmiş gözetim; `B006 [C]` değerli bir örtüyü koruma; `B007 [C]` deniz kabuğu süsü; `B008 [C]` hayvan gözetimi ve üreme malı; `B009 [C]` bir şeyi zorunlu hizmette kullanma. |
| ر ب ب | `B001 [A]` teselli ve nimeti yöneten Rablik; `B002 [B]` yetiştirme, eğitim ve tamamlama; `B003 [B]` ilahî olarak yetiştirilen bilgi ve hidayet; `B004 [C]` topluluk ve kolektif sorumluluk; `B005 [B]` yetimin bakımı ve velayeti; `B006 [C]` yiyecek hazırlama ve koruma; `B007 [B]` kalıcı mevcudiyet ve barınak sürekliliği; `B008 [C]` rızık taşıyan bulut ve yağmur; `B009 [C]` yenidoğan bağımlılığı ve hane bakımı; `B010 [C]` paketlenmiş talih ve fal aracı; `B011 [C/B]` koruyucu ahit ve emanet yükümlülüğü; `B012 [C]` bitki ve beslenme alt-katmanı; `B013 [C/B]` bol, sürdürücü su; `B014 [C]` toplanmış sürü ve pastoral rızık; `B015 [C]` gramatik nicelik ve kiplik; `B016 [B]` ihsanla cevaplanan ihtiyaç; `B017 [C]` denizcilik otoritesi ve rehberlik. |
| ق ل ي | `B001 [C]` hızlı ayrıştırıcı hareket; `B002 [B]` açıkça reddedilen kovulma; `B003 [A]` açıkça reddedilen tiksinti veya nefret; `B004 [C]` kavurma ve yiyecek hazırlama; `B005 [C]` sopa oyunu ve rekabetçi kuvvet; `B006 [C]` temizleyici alkali ve arınma. |
| ء خ ر | `B001 [B]` ilk evreyle karşılaştırılan sonraki evre; `B002 [C/B]` daha sonra gelen ertelenmiş hayır; `B003 [C]` geriye dönük mekânsal yönelim; `B004 [A]` daha iyi gelecek ufku olarak âhiret. |
| خ ي ر | `B001 [A]` faydalı hayır ve üstün değer; `B002 [B]` seçilmiş mükemmellik ve ahlâkî liyakat; `B003 [B]` daha iyi yolu ayırt etme ve seçme; `B004 [C/B]` hayır sayılan servet; `B005 [B]` ihsan ve armağan; `B006 [C]` hayvanı sığınağından çıkarma. |
| ء و ل | `B001 [A]` ilk veya önceki evre; `B002 [B]` nihai sonuç ve anlama dönüş; `B003 [B]` koruyucuya dönen hane ve bağımlılar; `B004 [B]` işleri düzelten gözetim/yönetim; `B005 [C]` son hâle doğru maddî koyulaşma; `B006 [C]` görünür dış çizgi ve görünüş; `B007 [C/B]` zaman içinde karşılaştırılan hâl; `B008 [C]` destek aracı veya tabut; `B009 [C]` hayvanın dağ sığınağı; `B010 [C]` niteliği zaman içinde koruyan kap; `B011 [C]` yalıtılmış yem bitkisi adı. |
| ع ط و | `B001 [C/B]` ilahî vermenin karşılığı olarak elle alma; `B002 [A]` Rabbin vaat edilmiş vermesi; `B003 [B]` bağımlılara fiilî hizmet ve bakım; `B004 [C]` ahlâken riskli işe girişme; `B005 [B]` yardım isteme ve bağımlı ihtiyaç; `B006 [C/B]` boyun eğen uyum ve kolaylık; `B007 [C]` güçle başkasını aşma. |
| ر ض و | `B001 [A]` ilahî vermeden sonra hoşnutluk; `B002 [B]` aranan bol ilahî rıza; `B003 [C/B]` karşılıklı rıza ve toplumsal uzlaşma; `B004 [B]` hoşnutsuzluktan tatmine çıkarma; `B005 [C]` başkasını yenme rekabeti; `B006 [B]` itaatkâr, sevgi dolu ve güvenilir karakter; `B007 [C]` rızadan türemiş özel adlar. |
| و ج د | `B001 [A]` muhatabı ardışık hâllerde bulma; `B002 [B]` yokluk yerine devam eden mevcudiyet; `B003 [B]` yoksulluğa karşı imkân ve kapasite; `B004 [B]` terk tesellisi içinde hissedilen keder ve sevgi; `B005 [C]` reddedilen ilişkisel durum olarak öfkeli hınç. |
| ي ت م | `B001 [A]` ebeveyn korumasından yoksun yetim; `B002 [B]` yalnızlık ve kırılgan tekillik; `B003 [B]` gaflet ve bakımın aksaması; `B004 [B]` gecikmiş veya esirgenmiş ihsan; `B005 [C/B]` desteksiz hane ve evlilik statüsü. |
| ء و ي | `B001 [A]` yetimi barınağa çekme; `B002 [B]` kırılganlığa şefkatle yönelme. |
| ض ل ل | `B001 [A]` yönlendirilmeden önce hidayetsiz olma; `B002 [C/B]` görünürdeki yokluk sırasında gizlenme veya kaybolma; `B003 [B]` kaybolup sonra bulunma; `B004 [C]` hafıza ve muhafaza kaybı; `B005 [C]` gözetim gerektiren başıboş hayvan. |
| ه د ي | `B001 [A]` yola ve hakikate yumuşak rehberlik; `B002 [B]` yönlendirilmiş rota ve amaçlı tarz; `B003 [C]` öndeki kılavuz ve öncelik; `B004 [B]` sevgiyle gönderilen lütuf armağanı; `B005 [C]` kutsal mekâna sunulan ritüel kurban; `B006 [C]` haneye götürülen gelin; `B007 [B]` sığınma ve korunan gözetim; `B008 [C]` güçsüzlükte destekli yürüme; `B009 [C]` zayıf ve donuk karakter etiketi; `B010 [B]` sakin, derli toplu ve etikçe ölçülü tavır; `B011 [C/B]` iletişimsel armağan ve karşılıklı şiir. |
| ع ي ل | `B001 [A]` yoksulluk ve maddî ihtiyaç; `B002 [B]` sürekli destek isteyen bağımlılar; `B003 [C]` dengesiz sallanan yürüyüş; `B004 [B]` açlık ve yetersiz beslenme; `B005 [C]` hayvanı ıssız yerde bırakma; `B006 [C]` Aylan özel adı; `B007 [C]` erkek sırtlan adı; `B008 [B]` yönünü şaşırmış kaybolmuşluk; `B009 [B]` kapasitesinin ötesinde bunalmışlık; `B010 [C/B]` kıtlıkla yoğunlaşan aşırı arzu. |
| غ ن ي | `B001 [A]` ilahî zenginleştirme ve yeterlilik; `B002 [B]` yetme, fayda sağlama ve ihtiyacı karşılama; `B003 [C/B]` sesli ifade ve övgü; `B004 [B]` istikrarlı mesken ve yerleşik mevcudiyet; `B005 [C]` statü veya güzellikle kadın bağımsızlığı; `B006 [C/B]` evlilik yoluyla hane yeterliliği ve koruma. |
| ق ه ر | `B001 [A]` yasaklanan, yetimi ezme ve aşağılama; `B002 [C]` ele geçiren ısıyla dönüşen yiyecek; `B003 [C]` sıcak ve besleyici yiyecek hazırlama; `B004 [C]` sert öğütme taşı ve araç; `B005 [C/B]` geriye çekilme ve terk; `B006 [C/B]` kırılgan ihtiyaç için bol saklanmış yiyecek; `B007 [C]` küçük canlıya ait özel terim. |
| س ء ل | `B001 [A]` isteyen kişi; `B002 [B]` ihtiyaç duyulan veya arzulanan talep; `B003 [B]` talebi merhamet ve rızıkla yerine getirme; `B004 [C/B]` karşılıklı soru ve insanî diyalog. |
| ن ه ر | `B001 [C]` akan nehir ve bolluk; `B002 [B]` duhâ yanında gündüzün açılması; `B003 [C/B]` daraltmak yerine açma ve genişletme; `B004 [A]` yasaklanan sert sözlü azarlama; `B005 [C]` kuş yavrusu ve büyüme evresi adı; `B006 [C]` gizli kapma ve zorlama; `B007 [C]` özel adlar ve kimlik; `B008 [C]` bulut ve hava alt-katmanı. |
| ن ع م | `B001 [A]` Rabbin ihsan ettiği nimet ve iyilik hâli; `B002 [B]` rahatlık ve kolay refah; `B003 [B]` nimeti övme ve olumlu değerlendirme; `B004 [B]` onay ve tanıklık mutabakatı; `B005 [C/B]` maddî servet ve rızık olarak hayvanlar; `B006 [C]` devekuşu yaban hayatı dalı; `B007 [C]` devekuşuna benzer adlandırılmış biçimler; `B008 [C]` dağılma ve göç imgesi; `B009 [C/B]` yumuşak rüzgâr ve duyusal rahatlık; `B010 [C/B]` ihsanı artırma ve uzatma; `B011 [B]` hoş karşılayan mesken ve iyi ikamet; `B012 [C]` yaya hizmet ve hareket; `B013 [B]` göz aydınlatan nimet, sevgi ve iyilik hâli. |
| ح د ث | `B001 [C/B]` yokluktan sonra yeni olay ve belirme; `B002 [C]` genç tazelik ve yenilik; `B003 [A]` Rabbin nimetini söyleme ve anlatma; `B004 [B]` kamusal olarak hatırlanan anlatıya dönüşme; `B005 [C]` zamanın felaketi ve olayı; `B006 [B]` nimeti açığa vurma ve bilinir kılma; `B007 [C/B]` kalbi ahlâkî berraklığa cilalama; `B008 [C/B]` doğru içgörüye yönelik içsel telkin. |

## İkincil aktivasyon tablosu

Bu tablo `07-secondary-expansion.json` içindeki 16 yeni veya güçlendirilmiş adayı gösterir. “Geçiş” sütunu, ilk aktivasyon etiketinden ikincil değerlendirmeye geçişi verir; değişmeyen etiketler de gerekçesi güçlendirilen okumalar olarak korunmuştur.

| Kök / branch | Geçiş | İkincil katkı ve sınır |
|---|---:|---|
| `ر ب ب B004` | `C → C/B` | Kişiye ulaşan Rabbanî bakımın, yetim ve isteyen üzerinden topluluk ölçeğinde sorumluluğa dönüşmesini görünür kılar; ordu, kabile veya sayısal kalabalık iddia etmez. |
| `ر ب ب B008` | `C → C/B` | Duhâ, çöken gece ve yeterlilik arasında görünmeyen rızık hazırlığını yağmur taşıyan bulut ekolojisiyle modeller; metinde literal bulut/yağmur yoktur. |
| `ر ب ب B013` | `C/B → C/B` | Sessiz birikimin daha sonra yeterliliğe dönüşmesini bol su imgesiyle güçlendirir; kuyu, nehir veya içme suyu yüzey olayı değildir. |
| `ض ح و B003` | `C/B → C/B` | Kuşluk öğünü ve erken otlatma dalı, açlık–yeterlilik–nimet hattına görünür olmadan hazırlanmış besin alt-katmanı ekler; hayvan ve mera literal değildir. |
| `ن ه ر B008` | `C → C/B` | Gündüz/gece, Rabbanî bakım ve zenginleştirme arasında hava-su bağlantısını destekler; 10. ayetteki `تَنْهَرْ`in yüzey anlamı azarlamadır. |
| `س ء ل B004` | `C/B → B` | İsteyeni susturmamanın olumlu karşılığını diyalog, cevap ve ilişkinin sürmesi olarak kurar; karşılıklı soru-cevap fiilen gerçekleşmiş sayılmaz. |
| `ن ه ر B003` | `C/B → B` | Sert sözün kapattığı erişime karşı “açma/genişletme”yi etkinleştirir; yara, kan akışı veya beden açıklığı ayrıntıları dışarıda kalır. |
| `ن ع م B004` | `B → B` | Nimeti sahip olunan nesneden, kabul edilen ve doğru tanıklıkla anlatılan iyiliğe dönüştürür; ayete `نعم` edatı eklenmez. |
| `ن ع م B011` | `B → B` | Barınma ve yeterliliği, yalnız örtü altına alınmaktan kalıcı aidiyet ve yaşanabilir meskene taşır; belirli bina ya da ülke öne sürmez. |
| `و د ع B004` | `C/B → B` | Terk etmemenin etik biçimini kırılgana karşı saldırmazlık ve düşmanca kopuştan sakınma olarak güçlendirir; antlaşma, savaş ve diplomasi literal değildir. |
| `ء و ل B004` | `B → B` | İlk ve sonraki evre arasındaki geçişi edilgin kronoloji olmaktan çıkarıp, alınan bakımı bugünkü toplumsal düzenlemeye çevirme işi yapar; siyasal makam iddia etmez. |
| `س ج و B003` | `C/B → B` | Gecenin yerleşmesini, tesellinin kalıcı ve ölçülü karaktere dönüşmesinin analoğu yapar; `سَجَىٰ` gramatik olarak muhatabı nitelemez. |
| `ح د ث B007` | `C/B → B` | Nimeti anlatmayı ahlâkî algıyı cilalayan ve kalbi diri tutan hatırlatma işleviyle genişletir; bıçak, metal ve silah çağrışımları alınmaz. |
| `خ ي ر B004` | `C/B → C/B` | “Hayır”ın servet kullanımını korur ama serveti, ihtiyaç gideren ve nimeti dolaştıran bir taşıyıcıyla sınırlar; üstün hayır maddî birikime indirgenmez. |
| `ق ه ر B006` | `C/B → C/B` | Ezme kapasitesinin tersine, kaynağın aç ve bağımlı için yiyecek korumaya yöneltilebileceğini gösterir; kap veya depolanmış erzak literal değildir. |
| `غ ن ي B003` | `C/B → C/B` | Yeterliliğin nimet anlatımıyla sesli ve duygulanımsal şükre dönüşmesini korur; şarkı, şiir, müzik veya ritüel icra iddia etmez. |

### İkincil mekanizma kümeleri

1. **hidden_ecology_of_unseen_provision — `C/B`:** `ض ح و → ل ي ل → س ج و → ر ب ب → ن ه ر → ع ي ل → غ ن ي → ن ع م`. Duhâ, çöken gece, bulut, biriken su, besin, yoksulluk, yeterlilik ve nimet; görünmeyen bakımın görünür rızka dönüşmesinin maddî analoğunu kurar.
2. **speech_keeps_need_open — `B`:** `س ء ل → ن ه ر → ع ط و → غ ن ي → ن ع م → ح د ث`. Talep ihtiyacı konuşulabilir kılar; azarlama erişimi kapatırken diyalog, cevap, fiilî destek ve doğru anlatım ilişkiyi açık tutar.
3. **collective_stewardship_from_received_care — `B`:** `و د ع → ر ب ب → ء و ل → ي ت م → ع ي ل → ع ط و → ه د ي`. Kırılganlıkta alınan emanet bakım, daha geniş bir topluluğa karşı gözetim ve sorumluluğa dönüşür.
4. **good_is_not_reducible_to_wealth — `B`:** `خ ي ر → ع ط و → ع ي ل → غ ن ي → ن ع م`. Servet “hayır”ın bir taşıyıcısı olabilir; fakat üstün hayır verme, bağımlıyı destekleme ve nimeti uzatma biçiminde tanımlanır.
5. **settled_disposition_becomes_public_ethic — `B`:** `س ج و → خ ي ر → ه د ي → ق ه ر → ن ه ر → ح د ث`. Gecenin dinginliği, ölçülü rehberlik, ezmeme, azarlamama ve doğru anlatımla kamusal ahlâka olgunlaşır.
6. **shelter_matures_into_habitable_belonging — `B`:** `ي ت م → و ج د → ء و ي → ر ب ب → غ ن ي → ن ع م`. Şefkatli bulma, ilk barınağı kalıcı gözetim, mesken ve aidiyete tamamlar.
7. **future_promise_as_repair_and_governance — `B`:** `ء و ل → ء خ ر → خ ي ر → ر ب ب → ع ط و → ر ض و`. Gelecek vaadi önceki kırılganlığı silmez; onu onarılmış bir düzene yerleştirir ve bugünkü sorumluluğu yönetir.
8. **voiced_favor_without_performance_claim — `C/B`:** `غ ن ي → ن ع م → س ء ل → ح د ث`. Yeterlilik sesli kabule ve şükür anlatımına dönüşür; bundan performans sanatı veya ritüel biçim çıkarılmaz.

## Graph-ready kök/düğüm ve kenar açıklaması

### Düğüm semantiği

- **Düğüm türü:** yalnız kök (`type=root`).
- **Düğüm kümesi (23):** `ض ح و`, `ل ي ل`, `س ج و`, `و د ع`, `ر ب ب`, `ق ل ي`, `ء خ ر`, `خ ي ر`, `ء و ل`, `ع ط و`, `ر ض و`, `و ج د`, `ي ت م`, `ء و ي`, `ض ل ل`, `ه د ي`, `ع ي ل`, `غ ن ي`, `ق ه ر`, `س ء ل`, `ن ه ر`, `ن ع م`, `ح د ث`.
- **Port/kanıt etiketi:** branch kimlikleri düğüm değildir; kenarın `source_branch` ve `target_branch` portlarıdır.
- **Yön:** aşağıdaki oklar anlatı akışını gösterir. Ontolojik veya sözlüksel nedensellik iddiası değildir.

### Birincil ve güçlü latent kenarlar

```text
ض ح و -> ل ي ل | ض ح و B001/B005 :: ل ي ل B001/B003 | kuşluk parlaklığı ile düzenli gece karşıtlığı | A/B
ل ي ل -> س ج و | ل ي ل B001/B003 :: س ج و B001/B002/B005 | gecenin dinginlik, örtü ve latent gözetim olarak çökmesi | A/B
س ج و -> و د ع | س ج و B004/B005 :: و د ع B001/B002/B005 | ölçülü sessizlikten terk değil güven ve emanete geçiş | B
و د ع -> ر ب ب | و د ع B001/B002/B005 :: ر ب ب B001/B002/B007/B011 | reddedilen terk, yetiştiren ve ahitli Rablik | A/B/C/B
و د ع -> ق ل ي | و د ع B001/B003 :: ق ل ي B002/B003 | terk, veda, kovma ve nefretin birlikte reddi | A/B
ء و ل -> ء خ ر | ء و ل B001/B002/B007 :: ء خ ر B001/B002/B004 | ilk evreden daha sonraki/âhiret sonucuna yöneliş | A/B/C/B
ء خ ر -> خ ي ر | ء خ ر B002/B004 :: خ ي ر B001/B002/B003 | sonraki ufkun ertelenmiş üstün hayrı | A/B
ر ب ب -> ع ط و | ر ب ب B001/B016 :: ع ط و B002/B003 | ihtiyacı vaat edilmiş verme ve fiilî bakımla karşılama | A/B
ع ط و -> ر ض و | ع ط و B002 :: ر ض و B001/B002/B004 | ilahî vermeden hoşnutluk ve onarıma | A/B
ر ب ب -> و ج د | ر ب ب B002/B007 :: و ج د B001/B002/B004 | yetiştiren mevcudiyetin hâli dikkatle bulması | A/B
و ج د -> ي ت م | و ج د B001/B004 :: ي ت م B001/B002 | dikkatli bulmanın yetim kırılganlığını tanıması | A/B
ي ت م -> ء و ي | ي ت م B001/B002/B003 :: ء و ي B001/B002 | açıkta kalmışlığın barınak ve şefkatle karşılanması | A/B
و ج د -> ض ل ل | و ج د B001 :: ض ل ل B001/B003 | bulmanın yönsüz ve kayıp hâli tanıması | A/B
ض ل ل -> ه د ي | ض ل ل B001/B003 :: ه د ي B001/B002/B004/B010 | kaybolmuşluktan yumuşak yön, armağan ve ölçülü tavra | A/B
و ج د -> ع ي ل | و ج د B001/B003 :: ع ي ل B001/B002/B004/B009 | yoksulluk, bağımlılık, açlık ve aşılmış kapasitenin görülmesi | A/B
ع ي ل -> غ ن ي | ع ي ل B001/B002/B004/B009 :: غ ن ي B001/B002/B004 | ihtiyacın yeterlilik, destek ve meskenle karşılanması | A/B
ي ت م -> ق ه ر | ي ت م B001/B002 :: ق ه ر B001/B005 | yetim kırılganlığından ezme ve bakımdan çekilme yasağına | A/B/C/B
س ء ل -> ن ه ر | س ء ل B001/B002/B003/B004 :: ن ه ر B003/B004 | konuşulabilir ihtiyacın diyalogla açılması, azarla kapatılmaması | A/B
ر ب ب -> ن ع م | ر ب ب B016 :: ن ع م B001/B010/B013 | cevaplanan ihtiyacın uzatılmış ve sevgi taşıyan nimete dönüşmesi | A/B
ن ع م -> ح د ث | ن ع م B001/B003/B004/B013 :: ح د ث B003/B004/B006/B007 | nimetin övgü, tanıklık, kamusal hafıza ve ahlâkî berraklık olarak anlatılması | A/B
```

### Keşif düzeyi kenarlar

```text
و د ع -> ر ب ب | و د ع B005 :: ر ب ب B011 | emanet bırakma ile koruyucu ahit/güven | C/B -> B kontrollü keşif
س ج و -> ر ب ب | س ج و B005 :: ر ب ب B002 | yerleşik gözetim ile yetiştirme ve tamamlama | B
و د ع -> و ج د | و د ع B003 :: و ج د B004 | veda ile keder, sevgi ve duygulanımsal ilgi | B
و ج د -> ء و ي | و ج د B004 :: ء و ي B002 | hissedilen şefkatin barınağa dönüşmesi | B
خ ي ر -> ن ع م | خ ي ر B005 :: ن ع م B001 | ihsan, patronaj ve dolaşan refah olarak nimet | B
ر ب ب -> ن ع م | ر ب ب B016 :: ن ع م B001 | ihtiyaba cevap veren ihsan ile Rablik | B
ع ط و -> ع ي ل | ع ط و B003 :: ع ي ل B002 | fiilî hizmet ile bağımlının sürekli bakımı | B
ع ط و -> س ء ل | ع ط و B005 :: س ء ل B001 | yardım talebi ile ifade edilmiş ihtiyaç | B
ع ط و -> غ ن ي | ع ط و B005 :: غ ن ي B002 | bağımlı talebin gerçekten yeterli destekle karşılanması | B
غ ن ي -> س ء ل | غ ن ي B002 :: س ء ل B003 | yeterlilik ile talebin merhametle yerine getirilmesi | B
ر ب ب -> ن ه ر | ر ب ب B008 :: ن ه ر B008 | rızık taşıyan bulut ile hava/su alt-katmanı | C/B
س ج و -> ر ب ب | س ج و B006 :: ر ب ب B013 | gece dinginliğindeki bolluk ile sürdürücü su | C/B
ض ح و -> ن ع م | ض ح و B003 :: ن ع م B005 | kuşluk merası ile hayvan/rızık nimeti | C/B
```

### Mekanik olarak güçlü fakat yerel olarak etkinleştirilmemiş kenarlar

```text
ع ط و -> ر ض و | ع ط و B007 :: ر ض و B005 | rekabetçi üstün gelme | C
ي ت م -> ه د ي | ي ت م B005 :: ه د ي B006 | evlilik statüsü ve gelinin haneye götürülmesi | C
ق ل ي -> ق ه ر | ق ل ي B004 :: ق ه ر B003 | kavurma, ısı ve yiyecek hazırlama | C
ض ح و -> ه د ي | ض ح و B004 :: ه د ي B005 | kurban ve kutsal mekâna sunu | C
ه د ي -> ن ه ر | ه د ي B011 :: ن ه ر B007 | edebiyat/şiir ile özel ad bağlantısı | C
```

## Most surprising discoveries

### 1. “Terk edilmedi” ifadesi, emanet edilmiş ahitli bakıma derinleşiyor

En güçlü keşif kenarı `و د ع B005 ↔ ر ب ب B011`dir. Terk etme kökünün içinde, bir şeyi gözetime “emanet bırakma” dalının bulunması şaşırtıcıdır. Açık terk anlamı olumsuzlandığında bu dal, muhatabın koruyucu Rablik içinde güvenilmiş bir sorumluluk olarak kaldığını düşündürür. Bu, `وَدَّعَكَ`ın yüzey anlamını “emanet etti” diye değiştirmez; terk edilmeme güvencesinin pozitif içeriğini emanet gözetimi, sadakat ve ahitle genişletir.

### 2. Çöken gece, faaliyetsizliğin değil görünmeyen gözetimin imgesi oluyor

`س ج و B005 ↔ ر ب ب B002`, yerleşmiş sessizliği yetiştirme, bakım ve tamamlama ile bağlar. Böylece sûrenin açılışındaki gece, ilahî faaliyetin durduğu zaman değil; görünür işaret azalsa da bakımın sürdüğü evredir. Bu bağlantı, açılış yeminin teselliye neden bu kadar uygun olduğunu ve son emirlerde bakımın güçsüz kişiye karşı neden kesilmemesi gerektiğini aynı mekanizmayla açıklar.

### 3. Reddedilen veda, yalnız mekânsal ayrılık değil; duygusal ilgisizlik ihtimalini de reddediyor

`و د ع B003 ↔ و ج د B004` veda ile keder/sevgiyi, `و ج د B004 ↔ ء و ي B002` ise hissedilen şefkatle barınağı birleştirir. Bu nedenle “Rabbin seni terk etmedi” güvencesi yalnız temasın sürmesi değildir: ilişki kaygıdan, sevgiden ve uygun yardım üretme kapasitesinden boşalmamıştır. Yetimi barındırma, bu duygulanımsal ilginin somut biçimidir.

### 4. Nimet, özel bir sahiplikten dolaşımdaki bakım ilişkisine dönüşüyor

`خ ي ر B005 ↔ ن ع م B001`, hayırlı ihsanı yardım, patronaj ve toplumsal refahla; `ر ب ب B016 ↔ ن ع م B001` ise karşılanan ihtiyacı Rabbanî nimetle bağlar. `ع ط و B003 ↔ ع ي ل B002` bu nimetin pratik biçimini bağımlı bakımında gösterir. Son ayette nimeti anlatmak bu yüzden yalnız kişisel şükür beyanı değildir; kendisine ulaşmış desteğin yetim ve isteyen için yeniden dolaşıma girmesini kabul etmektir. Buradaki karşılıklılık Allah’a eşit bir geri ödeme değil, alınan bakım biçiminin etik taklididir.

### 5. İsteyen kişi nimet akışının dışında bir kesinti değil, akışın sınandığı düğümdür

`ع ط و B005 ↔ س ء ل B001`, yardım istemeyi ifade edilmiş ihtiyaçla; `ع ط و B005 ↔ غ ن ي B002` ve `غ ن ي B002 ↔ س ء ل B003` ise talebi gerçekten yeten desteğe bağlar. Şaşırtıcı sonuç şudur: isteyen, nimetin dolaşımını bozan kişi değil, nimetin başkasına geçebildiği eşiktir. Sert azarlama bu devreyi tam ihtiyaç konuşulabilir olduğunda kapatır; diyalog ve karşılık ise açık tutar.

### 6. Duhâ ve gece arasında gizli bir rızık ekolojisi beliriyor

`ر ب ب B008 ↔ ن ه ر B008`, rızık taşıyan bulutla atmosferik suyu; `س ج و B006 ↔ ر ب ب B013`, gecenin yerleşik bolluğuyla birikmiş suyu; `ض ح و B003 ↔ ن ع م B005` ise kuşluk, otlak ve beslenmeyi bağlar. Bu küme, görünür nimetin öncesinde çalışan hava–su–besin döngüsünü, sûrenin “sessizlik terk değildir” fikrine maddî bir analog yapar. Metin bulut, kuyu, mera veya hayvan anlatmadığı için bu okuma `C/B` sınırında tutulmalıdır.

### Seçilmemiş fakat korunmuş yüksek-sürpriz adaylar

- `ع ط و B007 ↔ ر ض و B005`: güçle yarışıp üstün gelme ortaklığı yüksektir; fakat ilahî verme ve rıza bağlamı rekabetçi tahakkümü etkinleştirmez.
- `ي ت م B005 ↔ ه د ي B006` ve `ه د ي B006 ↔ غ ن ي B006`: evlilik/hane bağlantıları mekanik olarak güçlüdür; yüzeydeki yetimlik ebeveyn koruması kaybıdır, evlenmemişlik veya gelin transferi değildir.
- `ق ل ي B004 ↔ ق ه ر B002/B003`: pişirme ve ısı ortaklığı yerel mekanizmaya girmez.
- Yaban hayatı ve hayvan üretimi kümeleri (`ع ي ل B007 ↔ ن ع م B006`; `ن ه ر B005 ↔ ن ع م B006`; `ر ب ب B009 ↔ ن ه ر B005`) keşif rezervuarında `C` kalır.
- `ض ح و B004 ↔ ه د ي B005`, özel-ad kümeleri (`ل ي ل B004`, `ن ه ر B007`, `ر ض و B007`) ve `ه د ي B011 ↔ ن ه ر B007` yerel olarak etkin değildir. `فَحَدِّثْ` anlatmayı emreder; şiir, yazı, ritüel icra veya özel yer adı belirtmez.
- `س ج و B002 ↔ ض ل ل B002` içindeki gömme/gizleme çağrışımı, gecenin geçici örtüsü için fazla uzaktır.

## Açık sorular

1. `ٱلْءَاخِرَةُ` için `ء خ ر B004`ün doğrudan âhiret anlamı ile `ء خ ر B001/B002`nin “sonraki evre/ertelenmiş hayır” anlamları hangi ölçüde eşzamanlı tutulmalı; hangisi yorumun ana zaman ufku olmalıdır?
2. `ضَآلًّا`daki `ض ل ل B001` yüzey anlamı, biyografik ve teolojik aşırı yorumlara kaçmadan “yol bilgisine henüz yöneltilmemiş olma” şeklinde nasıl daha kesin ifade edilebilir?
3. `وَجَدَكَ` tekrarındaki `و ج د B004` duygulanımsal sevgi/keder dalı, ana mekanizmayı aydınlatacak kadar yerel denetime sahip mi; yoksa `B` yerine `C/B` ihtiyatı mı gerektirir?
4. `س ء ل B004`, `ن ه ر B003` ve `ن ع م B004`ün oluşturduğu “diyalog–açıklık–cevap” mekanizması, isteyenin maddî talebi ile bilgi sorusunu ayıran daha ayrıntılı bir söylem çözümlemesiyle sınanabilir mi?
5. `ر ب ب B008/B013`, `ن ه ر B008`, `س ج و B006` ve `ض ح و B003`ün gizli rızık ekolojisi, sûre içi yerel kontrolden çok mekanik tema ortaklığına mı dayanıyor? `C/B` statüsünü yükseltmek için ne tür metin-içi kanıt gerekir?
6. `ن ع م B011`in “yaşanabilir aidiyet” okuması, yetimin barındırılması ile zenginleştirmenin mekânsal boyutunu gerçekten birleştiriyor mu, yoksa modern “aidiyet” kavramını metne fazla mı taşıyor?
7. `ح د ث B007`nin kalbi cilalama işlevi, nimeti anlatmanın etik sonucu olarak güçlüdür; ancak branch’in silah/metal ayrıntılarından tamamen ayrıştırıldığını göstermek için ek sözlüksel denetim gerekir mi?
8. Besmele analiz çerçevesine dahil olduğu hâlde QAC branch envanterinin 1. ayetle başlaması, rahmet mekanizmasının kök/branch grafında yalnız çerçeve olarak kalmasına yol açıyor. Gelecek koşularda Besmele kökleri için ayrı, kaynak-temelli portlar sağlanmalı mı?

## Sonuç

S93:1–11’in en tutarlı bütüncül okuması, görünürlüğün azalmasını terk sanan korkuyu; geçmişte tekrar tekrar işlemiş uygun bakım örüntüsüyle gidermesidir. Gece sessiz olabilir, fakat Rabbanî gözetim sürer; sonraki ufuk daha hayırlıdır; yetimlik, yönsüzlük ve yoksunluk sırasıyla barınak, hidayet ve yeterlilikle karşılanmıştır. Bu hatırlama, muhatabı edilgin bir teselli alıcısı olarak bırakmaz: aynı bakım mantığını yetime karşı güç kullanmamak, isteyeni sözle kapatmamak ve nimeti doğru biçimde görünür kılmak suretiyle topluma aktarmasını ister. İkincil aktivasyonların en güçlü katkısı da budur: sûrenin merkezindeki nimet, saklanan bir kazanım değil; açık tutulan ilişki içinde dolaşan bakım kapasitesidir.
