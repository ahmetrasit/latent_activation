# S94:1–8 (İnşirâh/Eş-Şerh) — Nihai Bütünleştirme Raporu

## Kapsam ve yöntem notu

Bu rapor yalnız S94:1–8 için sağlanan `00-surah-text.json`, `01-passage.json`, `02-branches.json`, `03-candidate-bridges.json`, `05-activation-pass.json`, `06-mechanism.md`, `07-secondary-expansion.json`, `08-graph.json` ve `10-discovery-ranking.json` girdilerini bütünleştirir. QAC kelime sırası, morfoloji ve kök çözümlemesinde; `00-surah-text.json` tilavet metninde esas alınmıştır. Besmele analiz çerçevesine dahildir; ancak branch envanteri 1. ayetle başladığı için Besmele’ye mahsus kök veya branch kimliği icat edilmemiştir. On dört kökün tamamı `resolved` durumundadır; eksik veya dışarıda bırakılmış kök yoktur.

> بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ  
> أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ  
> وَوَضَعْنَا عَنكَ وِزْرَكَ  
> ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ  
> وَرَفَعْنَا لَكَ ذِكْرَكَ  
> فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا  
> إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا  
> فَإِذَا فَرَغْتَ فَٱنصَبْ  
> وَإِلَىٰ رَبِّكَ فَٱرْغَب

## Kısa nihai rapor

Sûrenin birincil mekanizması **ilahî rahatlatma → onarılmış kapasite → yeniden ve doğru yöne çevrilmiş çaba** çizgisidir. İlk ayet, göğsün açılıp genişletildiğini bildirir (`ش ر ح B003`; `ص د ر B001`). Dış koşul değiştirilmeden önce kişinin iç dünyasında anlama, kabul ve hareket için yer açılır. İkincil `ش ر ح B001/B005`, bu genişliği açıklık ve motivasyon alanına taşır: açılan kapasite yalnız rahatlamak için değil, anlamak ve yönelmek içindir.

Ardından ezici yük indirilir (`و ض ع B001`; `و ز ر B002`). Yükün ağırlığı soyut bırakılmaz: sırtı gıcırdatmıştır (`ن ق ض B005`; `ظ ه ر B002`). Göğsün genişletilmesi ile sırtın rahatlatılması birlikte, bütün kişinin yeniden işler hâle getirilmesidir. Sûre yükü inkâr etmez; taşıyıcı yapının sınırına kadar ulaştığını kabul eder ve rahatlamayı bu yapıyı onaran ilahî fiil olarak sunar.

Yükün aşağı indirilmesine, şerefli anılışın yukarı kaldırılması eşlik eder (`ر ف ع B002`; `ذ ك ر B007`). Böylece hareket yalnız ağırdan hafife değil, sıkışmış veya alçalmış durumdan tanınan bir değere doğrudur. İkincil dallar bu yükselişi sözlü anılma, kamusal aktarım ve yenilenen dikkatle genişletir (`ر ف ع B005/B010`; `ذ ك ر B004/B009`); fakat bunu muhatabın kendini pazarlaması olarak değil, ilahî yükseltmenin dolaşıma giren tanıklığı olarak sınırlar.

İlk dört ayetteki fiiller, iki kez tekrarlanan “zorlukla beraber kolaylık vardır” ilkesini somutlaştırır (`ع س ر B001`; `ي س ر B001`). `مَعَ`, kolaylığı yalnız zorluk bittikten sonraya ertelemez; zorluğun alanında onunla birlikte bulunan kullanılabilir bir açıklık olarak kurar. Göğüs darlık içinde genişletilir, gıcırdayan sırtın yükü indirilir ve aşağı alınan ağırlıkla beraber anılış yükseltilir. Kolaylık, zorluğu yok saymak değil, onun içinde hareket kapasitesi açmaktır.

Bu yüzden rahatlamanın sonucu kalıcı hareketsizlik değildir. Bir iş tamamlandığında veya kişi ondan serbest kaldığında (`ف ر غ B001`), yeni bir emeğe doğrulması emredilir (`ن ص ب B001/B004`). `ف ر غ B006`, boşalan dikkatin adanmış niyete dönüşmesini açıklar. Kolaylık, kişiyi görevden muaf kılan son durak değil; eski ezici yük olmadan yeni bir göreve girişebilmesini sağlayan geçiş kapasitesidir.

Son emir bu çabanın hedefini belirler: arzu ve yöneliş Rabbe çevrilmelidir (`ر ب ب B001`; `ر غ ب B001`). Rablik, sahiplik yanında yetiştirme ve tamamlama işlevini de taşır (`ر ب ب B002/B003`). Böylece sûre üretkenliği kendi başına kutsamaz. Açılan göğüs, indirilen yük, yükseltilen anılış, zorluk içindeki kolaylık ve yenilenen emek; ancak arzunun Rabbe yönelmesiyle tek bir anlamlı çevrime dönüşür.

Besmelenin rahmet çerçevesi, rahatlatma ile çabanın karşıt olmadığını gösterir. Rahmet, emeği iptal etmez; kişinin ezilmeden emek verebilmesi için kapasitesini onarır. Sûrenin bütüncül iddiası bu nedenle “zorluktan sonra dinlenme”den daha güçlüdür: Zorluğun içinde açılan kolaylık, yük altında bozulan taşıma sistemini onarır; onarılan kişi yeni işe doğrulur ve bütün enerjisini Rabbe yönelmiş arzuyla toplar.

### Yorum sınırları

- `A`, yüzey ve yakın bağlamın doğrudan taşıdığı; `B`, güçlü ikincil; `C/B`, kontrollü fakat ihtiyatlı latent; `C`, geniş keşif rezervuarında korunan fakat yerel mekanizmaya alınmayan etikettir. Kaynaktaki üç `S` etiketi de aynen korunmuş, başka bir sınıfa çevrilmemiştir.
- İkincil dallar yüzey anlamını değiştirmez: `وَضَعْنَا` “emanet ettik”, `أَنقَضَ` hayvan sesi, `يُسْرًا` servet vaadi veya `فَٱرْغَب` maddî ödül talebi yapılmaz.
- `10-discovery-ranking.json`, 3.005 aday arasından sürpriz değeri yüksek mekanik bir inceleme kuyruğudur; yorum hükmü veya eleme aracı değildir. Yalnız “Most surprising discoveries” bölümü seçicidir.

## Aktive edilmiş branch tablosu

Envanter muhasebesi: **14 kök, 146 branch; A=14, B=15, C/B=12, C=102, S=3.** Aşağıdaki tablo seçici değildir; `05-activation-pass.json` içindeki bütün aktivasyon rezervuarını korur.

| Kök | Branch’ler ve aktivasyon rolleri |
|---|---|
| ش ر ح | `B001 [B]` açıklama ve açığa çıkarma alt-katmanı; `B002 [C]` maddî açma ve kesme; `B003 [A]` kabul kapasitesi için ilahî olarak genişletilen göğüs; `B004 [C]` bedensel açılma ve üreme; `B005 [C/B]` genişleyen arzu; `B006 [C]` koruma ve muhafaza. |
| ص د ر | `B001 [A]` anatomik ve içsel göğüs; `B002 [C]` ön, üst ve başta olma yönelimi; `B003 [C]` varıştan sonra ayrılış; `B004 [C]` gramatik masdar veya köken; `B005 [C]` otoriteyle servete el koyma; `B006 [C]` pay veya miktar. |
| و ض ع | `B001 [A]` yükü aşağı koyma ve kaldırma; `B002 [C]` taşınan gebeliğin bırakılması/doğum; `B003 [C]` hayvanın hızlı yolculuğu; `B004 [C]` sermaye kaybı ve azalması; `B005 [C/B]` yükseltilen şöhret karşısında alçaltılmış derece; `B006 [C]` yerleşmiş insanlar veya bırakılmış yükler; `B007 [C]` otlakta yerleşen hayvanlar; `B008 [C]` giysiye pamuk yerleştirme; `B009 [C]` kadının örtüsünü bırakması; `B010 [C]` emanet bırakma; `B011 [C]` karşılıklı anlaşma veya düzenleme; `B012 [C]` kararlılık eksikliği veya kadınsı tavır; `B013 [C]` binmek için devenin boynunu alçaltması. |
| و ز ر | `B001 [C]` sığınak ve tahkim edilmiş koruma; `B002 [A]` muhatabın taşıdığı ağır yük; `B003 [C]` savaş silahı ve teçhizatı; `B004 [B]` başkasının yükünü taşıyan yardımcı; `B005 [C]` ele geçirme ve götürme; `B006 [C]` kişiye üstün gelme; `B007 [C]` kuşanma veya binme. |
| ن ق ض | `B001 [B]` bağlanmış veya kurulmuş şeyi çözme; `B002 [C]` yolculuktan yıpranmış deve; `B003 [C]` toprağın mantar için yarılması; `B004 [C]` iyileşme veya yerleşmeden sonra yeniden açılma; `B005 [A]` ağır yük altında sırtın gıcırdaması; `B006 [C]` tıklama, çağrı ve hayvan sesleri; `B007 [C]` naqad adlı bitki; `B008 [C]` kararsız at üreme durumu. |
| ظ ه ر | `B001 [C/B]` görünme ve açığa çıkma; `B002 [A]` yük taşıyan anatomik sırt; `B003 [C]` yeryüzünün yükselmiş yüzeyi; `B004 [C]` öğle vakti; `B005 [C/B]` yük taşıyan binek veya hayvan; `B006 [B]` müttefik desteği ve güçlendirme; `B007 [C/B]` üstünlük ve galip gelme; `B008 [C]` öğrenme ve bilgiye erişme; `B009 [C]` belirgin/çıkık göz; `B010 [C]` zıhâr evlilik formülü; `B011 [C]` arka taraf tüy malzemesi; `B012 [C/B]` bir şeyi arkaya koyup bırakma; `B013 [C]` kişiden utanç veya kınamanın kaldırılması; `B014 [C]` destek için hane kaynakları; `B015 [C]` kara yolu ve dış bölge; `B016 [C]` destekçi grup veya yardımcılar; `B017 [C]` topluluk içinde bulunma; `B018 [C]` meseleyi her yönden çevirip inceleme; `B019 [C]` kalpte korunan bilgi; `B020 [C]` giysi veya zırhı kat kat giyme; `B021 [C]` tedbir ve ek azık alma; `B022 [C]` birbirine sırt çevirme; `B023 [C]` artan servetten verme; `B024 [C/B]` gurur kaynağı olarak gösterilen şeref. |
| ر ف ع | `B001 [B]` literal kaldırma ve yükseltme; `B002 [A]` derece ve şöhreti yükseltme; `B003 [C]` hayvan yolculuğunu hızlandırma; `B004 [C]` meseleyi otoriteye sunma; `B005 [B]` haberi yayma ve bilinir kılma; `B006 [C]` hasadı kaldırma; `B007 [C]` sütü memede tutma; `B008 [C]` kadın bedenini büyük gösteren dolgu; `B009 [C]` bağı kaldıran ip; `B010 [C/B]` sesi yükseltme; `B011 [C]` kara üzerinden yükselerek ilerleme; `B012 [C]` gramatik ref‘/merfûluk. |
| ذ ك ر | `B001 [C]` erkek cinsiyeti ve üreme; `B002 [C]` sertlik, keskinlik ve güç; `B003 [C/B]` unutuştan sonra hatırlama ve tutma; `B004 [B]` sözlü anma ve adlandırma; `B005 [B]` Allah’ı anma, övgü ve dua; `B006 [C/B]` vahyedilmiş kitap veya dinî metin; `B007 [A]` şerefli anılış ve iyi şöhret; `B008 [C]` hukukî hakkın yazılı belgesi; `B009 [B]` hatırlatma ve dikkati yenileme. |
| ع س ر | `B001 [A]` zorluk, güçlük ve şiddet; `B002 [B]` maddî darlık ve imkânsızlık; `B003 [C]` darlıktaki borçluya baskı; `B004 [B]` zorlaştırma, direnç ve engel; `B005 [C]` sol taraf ve solaklık; `B006 [C]` zor doğum; `B007 [C]` o yıl gebe kalmayan dişi deve; `B008 [C]` hazırlık öncesi alma veya binme; `B009 [C]` koşan hayvanın kalkık kuyruğu; `B010 [C]` uğursuz gün; `B011 [C]` dağınık veya ardışık hareket; `B012 [C]` varlık veya yer özel adları; `B013 [S]` ahşap fırlatma oyunu. |
| ي س ر | `B001 [A]` zorlukla beraber açılan kolaylık; `B002 [C]` küçük veya az miktar; `B003 [B]` bolluk, refah ve geniş imkân; `B004 [C]` sol taraf ve sol el; `B005 [C]` harekette hafiflik ve uysallık; `B006 [C]` hayvanlarda süt ve yavru artışı; `B007 [C]` kumar okları ve kurban devesinin paylaştırılması; `B008 [C]` ayrı çizgiler veya bedensel işaretler; `B009 [C]` aşağı doğru burma veya yüz hizasında hamle; `B010 [S]` Yusr/Yasar özel adı veya yer adı; `B011 [S]` Yasar adlı genç adam. |
| ف ر غ | `B001 [A]` işi bitirme ve meşguliyetten serbest kalma; `B002 [C]` kabı dökme ve boşaltma; `B003 [C]` hareket veya etkide genişlik; `B004 [C]` öcü alınmamış kan; `B005 [C]` meni ve üreme sıvısı; `B006 [B]` kendini adama ve niyeti yöneltme. |
| ن ص ب | `B001 [B]` ayağa kalkma veya kendini doğrultma; `B002 [C]` ibadet veya kurban için dikili taş; `B003 [C]` dik sınır işareti veya havuz taşı; `B004 [A]` emek, gayret ve yorgunluk; `B005 [C]` ayrılmış pay; `B006 [C]` sabit temel, tutamak veya eşik miktarı; `B007 [C]` gramatik nasb/mef‘ûllük; `B008 [C]` düşmanlık veya savaşla açıkça yüzleşme; `B009 [C]` yüksek sesli şarkı veya ezgi; `B010 [C]` hafif bir günlük yolculuk. |
| ر ب ب | `B001 [A]` egemen ve sahip olarak Rab; `B002 [B]` yetiştirme, onarma ve tamamına erdirme; `B003 [C/B]` ilahî temelli bilgi ve öğretim; `B004 [C]` büyük grup veya konfederasyon; `B005 [C]` bakılan çocuk veya bakıcı; `B006 [C]` koruyucu koyu şurup/hazırlık; `B007 [C]` kalma, yerleşme ve sürme; `B008 [C]` katmanlı yağmur bulutu; `B009 [C]` yeni doğurmuş sütlü koyun; `B010 [C]` fal okları demeti veya kabı; `B011 [C]` ahit, taahhüt ve koruma; `B012 [C]` kalıcı yeşil bitki; `B013 [C]` bol su; `B014 [C]` yaban sığırı veya deve sürüsü; `B015 [C]` rubba/rubbamâ edatı; `B016 [C]` ihtiyaç, bağlayıcı düğüm veya ihsan; `B017 [C]` denizcilerin reisi. |
| ر غ ب | `B001 [A]` arzu ve yönelişi Rabbe çevirme; `B002 [C]` genişlik, ferahlık veya geniş oyuk; `B003 [C]` oburluk ve güçlü iştah; `B004 [C/B]` bol ve arzu edilir armağan. |

## İkincil aktivasyon tablosu

Bu tablo `07-secondary-expansion.json` içindeki 18 yeni veya güçlendirilmiş adayı gösterir. Değişmeyen etiketler, yerel gerekçesi ikincil geçişte ayrıca pekiştirilen branch’lerdir.

| Kök / branch | Geçiş | İkincil katkı ve sınır |
|---|---:|---|
| `ش ر ح B005` | `C/B → B` | Açılan göğsü, son ayette Rabbe yöneltilen arzunun motivasyon kapasitesiyle birleştirir; dünyevî edinme ayrıntısı hedef yapılmaz. |
| `ر غ ب B002` | `C → C/B` | Göğüs açıklığı, kolay hareket ve biten işten doğan mekân için fiziksel genişlik analoğu sunar; kap, geniş arazi veya at hareketi literal değildir. |
| `ر غ ب B003` | `C → C/B` | Yoğun arzunun oburluğa dönüşebileceği negatif sınırı gösterir; yönelişin Rabbe çevrilmesi iştahı disipline eder, yeme olayı anlatılmaz. |
| `و ز ر B001` | `C → C/B` | Yükün kaldırılmasını, kişinin kendi içine kapanması değil koruyucu sığınağa yönelmesi olarak genişletir; dağ ve kale ayrıntıları alınmaz. |
| `ظ ه ر B016` | `C → C/B` | Gıcırdayan sırtın tek başına taşımak zorunda olmadığını; destekçi topluluk ve sadakat ihtimalini açar. Kabile, ordu veya belirli cemaat yoktur. |
| `ن ق ض B006` | `C → C/B` | İstemsiz yük sesinden, yükseltilmiş ve kamusal anılışın sesine geçişi korur; hayvan çağrısı ve azarlama ayrıntıları dışarıda kalır. |
| `ر ف ع B005` | `B → B` | Yükseltilen anılışı statünün yanında iletim, haber ve tanıklık olarak kurar; muhatabın öz-reklamını ima etmez. |
| `ر ف ع B010` | `C/B → B` | Sırtın gıcırtısından duyulabilir anılışa geçişte sesi yükseltmeyi etkinleştirir; bağırma, melodi veya belirli konuşmacı çıkarılmaz. |
| `ذ ك ر B004` | `B → B` | Şerefli şöhreti sözlü anma, adlandırma ve tanıklık yoluyla toplumsal dolaşıma sokar; kaynak ilahî yükseltmedir. |
| `ع س ر B002` | `B → B` | Zorluğa toplumsal-ekonomik darlık boyutu ekler; imkân yokluğunun eylem kapasitesini daralttığını gösterir, borç işlemi anlatmaz. |
| `ي س ر B003` | `B → B` | Kolaylığın somut fakat tek olmayan biçimi olarak geniş imkânı korur; `yusr` servet vaadine indirgenmez. |
| `ظ ه ر B023` | `C → C/B` | Onarılan taşıma kapasitesini, artandan başkasına fayda verme ihtimaline dönüştürür; zekât, alıcı veya maddî zenginlik yüzey iddiası değildir. |
| `ر غ ب B004` | `C/B → C/B` | İlâhî genişletme, rahatlatma ve kolaylığın ardından arzu edilir armağan kutbunu korur; emir armağana değil Rabbe yönelir. |
| `و ض ع B010` | `C → C/B` | Kaldırılan yükten boşalan kapasitenin amaçsız kalmayıp güven ilişkisi içinde emanet edilmesi analoğunu sunar; 2. ayet hukukî depozito değildir. |
| `ر ب ب B011` | `C → C/B` | Rahatlama ve yeni emeği özerk üretkenlikten çıkarıp güven, koruma ve ahit ilişkisine yerleştirir; sözleşme hukuku veya diplomasi anlatılmaz. |
| `ظ ه ر B013` | `C → C/B` | Yükün indirilmesi ve anılışın yükseltilmesini kimlik düzeyinde utanç/kınamanın kalkmasıyla genişletir; yük suçla özdeşleştirilmez. |
| `ظ ه ر B012` | `C/B → B` | Eski yükü arkada bırakmayı sıra ve öncelik olarak etkinleştirir; sorumluluğu ihmal etme veya küçümseme anlamları engellenir. |
| `ن ص ب B005` | `C → C/B` | Belirsiz kolaylığın kullanılabilir bir pay olarak yeni eylemi mümkün kılması analoğunu sunar; hukukî hak, miras veya ölçülü miktar vaat edilmez. |

### İkincil mekanizma kümeleri

1. **opened_capacity_becomes_directed_desire — `B`:** `ش ر ح → ص د ر → ي س ر → ف ر غ → ن ص ب → ر غ ب → ر ب ب`. İç genişleme yer açar; kolaylık ve bitiriş bu alanı kullanılabilir kılar; emek onu doldurur; arzu tek ve Rabbe dönük yön verir.
2. **strain_sound_becomes_public_testimony — `B`:** `و ز ر → ن ق ض → ظ ه ر → ر ف ع → ذ ك ر`. Sırt önce yükün istemsiz sesini çıkarır; rahatlamadan sonra ses, yükseltilmiş anılışa ve kamusal tanıklığa dönüşür.
3. **burden_relief_as_refuge_and_support — `B`:** `و ض ع → و ز ر → ظ ه ر → ر ب ب`. Yük kaldırma, yalnız eksiltme değil; sığınak, paylaşılan taşıma, koruyucu destek ve Rabbe güven içinde ilişkisel rehabilitasyondur.
4. **vertical_change_repairs_dignity — `B`:** `و ض ع → ظ ه ر → ر ف ع → ذ ك ر`. Ezici ağırlığın ve alçalmış konumun kalkması, şeref ve hatırlanan itibarın yükselmesiyle kimliği onarır; yük “suç” diye tanımlanmaz.
5. **economic_ease_as_shareable_surplus — `C/B`:** `ع س ر → ي س ر → ظ ه ر → ن ص ب → ر غ ب`. Darlık ve geniş imkân kutupları, kaynağın paylaşılan faydaya dönüşmesi ihtimalini açar; servet ve sadaka yalnız analojidir.
6. **freed_capacity_is_entrusted_not_ownerless — `C/B`:** `و ض ع → ر ب ب → ف ر غ → ن ص ب → ر غ ب`. Yükten boşalan kapasite sahipsiz değildir; güven ve amaç içinde yeni emeğe tahsis edilir ve Rabbe yönelir.
7. **desire_disciplined_against_appetite — `B`:** `ش ر ح → ظ ه ر → ف ر غ → ر غ ب → ر ب ب`. Genişleme motivasyonu artırır ama nesnesini belirlemez; Rabbe yöneliş arzuyu oburluk ve armağan saplantısından ayırır.
8. **ease_as_opening_for_work_not_inactivity — `B`:** `ع س ر → ي س ر → ف ر غ → ن ص ب → ر غ ب`. Kolaylık engel içinde kullanılabilir açıklıktır; tamamlanma dikkati serbest bırakır, fakat bu serbestlik doğrulmuş emek ve yönelmiş arzuya geçer.

## Graph-ready kök/düğüm ve kenar açıklaması

### Düğüm ve port semantiği

- **Düğüm türü:** yalnız kök (`type=root`).
- **Düğüm kümesi (14):** `ش ر ح`, `ص د ر`, `و ض ع`, `و ز ر`, `ن ق ض`, `ظ ه ر`, `ر ف ع`, `ذ ك ر`, `ع س ر`, `ي س ر`, `ف ر غ`, `ن ص ب`, `ر ب ب`, `ر غ ب`.
- **Portlar:** branch kimlikleri düğüm değil; kenarların kaynak/hedef kanıt portlarıdır.
- **Ok yönü:** anlatısal ve mekanizma yönüdür; sözlüksel veya ontolojik nedensellik iddiası değildir.

### Birincil ve güçlü latent kenarlar

```text
ش ر ح -> ص د ر | ش ر ح B001/B003/B005 :: ص د ر B001 | göğüs genişlemesi, açıklık, kabul ve geniş motivasyon | active/latent
ص د ر -> ظ ه ر | ص د ر B001 :: ظ ه ر B002/B005/B006 | göğüs ve sırtın kabul, yük ve destek sistemi | active/latent
و ض ع -> و ز ر | و ض ع B001/B005 :: و ز ر B002/B004 | ağır yükün indirilmesi ve yük paylaşan yardım | active/latent
و ز ر -> ن ق ض | و ز ر B002 :: ن ق ض B001/B005 | yük basıncının gıcırtıya dönüşmesi ve bağın çözülmesi | active/latent
ن ق ض -> ظ ه ر | ن ق ض B005/B006 :: ظ ه ر B002/B005 | işitilebilir zorlanmanın yük taşıyan sırtta yerleşmesi | active/latent
و ض ع -> ر ف ع | و ض ع B001/B005 :: ر ف ع B001/B002 | yük/alçalmış hâl aşağı inerken derece ve anılışın yükselmesi | active/latent
ر ف ع -> ذ ك ر | ر ف ع B002/B005/B010 :: ذ ك ر B004/B007 | yükselen şöhretin şerefli ve sözlü anılışla dolaşması | active/latent
ش ر ح -> ذ ك ر | ش ر ح B001 :: ذ ك ر B006/B009 | açıklığın öğretim, hatırlatma ve yenilenen dikkate açılması | latent
ع س ر -> ي س ر | ع س ر B001/B002/B004 :: ي س ر B001/B003/B005 | şiddet, darlık ve engelle beraber açıklık, imkân ve hareket | active/latent
ع س ر -> ن ص ب | ع س ر B001 :: ن ص ب B004 | zorluk alanında dayanma ve emek | active
ي س ر -> ف ر غ | ي س ر B001 :: ف ر غ B001 | kolaylığın işi bitirmek için geçiş kapasitesi açması | active
ف ر غ -> ن ص ب | ف ر غ B001/B006 :: ن ص ب B001/B004 | bitirişten adanmış niyet, doğrulma ve yeni emeğe | active/latent
ف ر غ -> ر غ ب | ف ر غ B006 :: ر غ ب B001 | boşalan dikkatin tek hedefe yönelmiş arzuya dönüşmesi | active/latent
ر ب ب -> ر غ ب | ر ب ب B001/B002/B003 :: ر غ ب B001 | egemen ve yetiştiren Rabbin arzunun açık hedefi olması | active/latent
ش ر ح -> ر غ ب | ش ر ح B005 :: ر غ ب B001 | içsel geniş arzunun Rabbe dönük yönelişte tamamlanması | latent
```

### Keşif düzeyi kenarlar

```text
ر ف ع -> ذ ك ر | ر ف ع B005 :: ذ ك ر B004 | yayılan haber ile sözlü tanıklık ve anma | B
ش ر ح -> ر غ ب | ش ر ح B005 :: ر غ ب B001 | genişleyen arzu ile son yöneliş | B
و ز ر -> ظ ه ر | و ز ر B004 :: ظ ه ر B006 | yük paylaşan yardımcı ile sırt desteği ve işbirliği | B
ظ ه ر -> ر غ ب | ظ ه ر B023 :: ر غ ب B004 | artandan verme ile arzu edilir bol fayda | C/B
ي س ر -> ر غ ب | ي س ر B003 :: ر غ ب B004 | geniş imkân ile arzu edilir rızık/fayda | B + C/B
ع س ر -> ر غ ب | ع س ر B002 :: ر غ ب B004 | maddî darlığın arzu edilir rızkın kıtlık kutbu olması | B + C/B
و ض ع -> ر ب ب | و ض ع B010 :: ر ب ب B011 | bırakılan emanet ile ahitli koruma | C/B
```

### Mekanik olarak güçlü fakat yerel olarak etkinleştirilmemiş kenarlar

```text
ع س ر -> ي س ر | ع س ر B005 :: ي س ر B004 | sol/sağ yönelimi ve eşseslilik | C
ش ر ح -> ف ر غ | ش ر ح B004 :: ف ر غ B005 | üreme/cinsellik ortaklığı | C
ي س ر -> ن ص ب | ي س ر B007 :: ن ص ب B002 | kumar oku ve kurban taşı/ritüel | C
و ز ر -> ن ص ب | و ز ر B003 :: ن ص ب B008 | savaş teçhizatı ve düşmanlık | C
ص د ر -> ر ف ع | ص د ر B003 :: ر ف ع B011 | göç ve yolculuk | C
ر ف ع -> ن ص ب | ر ف ع B012 :: ن ص ب B007 | gramatik ref‘ ve nasb | C
```

## Most surprising discoveries

### 1. Yükseltilen anılış, statüden kamusal tanıklığa dönüşüyor

En güçlü yerel keşif kenarı `ر ف ع B005 ↔ ذ ك ر B004`tir. Haberi yayma ile sözlü anma; iletişim, konuşma ve tanıklık ortaklığında birleşir. `ر ف ع B010` duyulabilir yükselişi, `ذ ك ر B007` ise yüzeydeki şerefli anılışı korur. Şaşırtıcı sonuç, yükseltilen değerin yalnız üst bir dereceye yerleştirilmemesi; söz ve tanıklık yoluyla dolaşıma girmesidir. Bu okuma `ذِكْرَكَ`ı tek bir söze indirgemez ve öz-reklam iddia etmez.

### 2. Sûrenin başında açılan göğüs, sonunda yöneltilen arzu oluyor

`ش ر ح B005 ↔ ر غ ب B001`, genişleyen arzuyu duygu, motivasyon, niyet ve bağlılık üzerinden Rabbe yönelmiş iştiyakla bağlar. Sayısal olarak en yüksek sürpriz olmasa da yapısal olarak sûrenin iki ucunu birleştirir: İlâhî fiil iç dünyada yer açar; son emir bu yerin neyle doldurulacağını belirler. `نَشْرَحْ` “arzu etmek” demek değildir; ikincil dal, açılan kapasitenin işlevini açıklar.

### 3. Yükün kaldırılması, yalnız hafifleme değil, yalnız taşımaktan kurtulmadır

`و ز ر B004 ↔ ظ ه ر B006`, başkasının yükünü taşıyan yardımcıyı sırt desteği, işbirliği ve sadakatle bağlar. Açık yük sırtı gıcırdatırken, ikincil ağ onun ilişkisel tersini üretir: taşıyıcının yalnızlığı kırılır ve yük paylaşılır. `ظ ه ر B016`, bu desteğin topluluk ihtimalini korur; fakat sûre belirli bir kabile, ordu veya örgüt söylemez.

### 4. Kolaylık, paylaşılabilir fazlaya dönüşebilen bir imkân ekonomisi taşıyor

`ظ ه ر B023 ↔ ر غ ب B004`, artan servetten vermeyi arzu edilir bol faydayla; `ي س ر B003 ↔ ر غ ب B004`, geniş imkânı bu faydayla; `ع س ر B002 ↔ ر غ ب B004` ise kıtlık kutbuyla bağlar. Böylece zorluk/kolaylık çifti toplumsal-ekonomik bir analog kazanır: açılan kapasite yalnız kişinin rahatlığına kapanmayıp başkasına fayda olacak fazlaya dönüşebilir. Metin sadaka emretmediği ve maddî zenginlik vaat etmediği için bu hat `C/B` sınırında kalır.

### 5. Aşağı koymak, boşta bırakmak değil koruma içinde emanet etmek olabilir

`و ض ع B010 ↔ ر ب ب B011`, emanet bırakmayı ahit, güven ve korumayla birleştirir. Birincil anlamda yük kaldırılmıştır; ikincil analoji ise bundan doğan serbest kapasitenin sahipsiz veya amaçsız kalmadığını söyler. Bitirilen işten sonra yeni emeğe yönelme ve Rabbe arzu, bu kapasiteyi güven ilişkisi içinde yeniden tahsis eder. Bu kenar `وَضَعْنَا`yı “emanet ettik”e veya sûreyi sözleşme hukukuna dönüştürmez.

### Seçilmemiş fakat rezervuarda korunan yüksek-sürpriz adaylar

- `ع س ر B005 ↔ ي س ر B004` sol/sağ bedensel yönelim eşsesliliğidir; burada zorluk ve kolaylığın anlamı değildir.
- Üreme/cinsellik (`ش ر ح B004 ↔ ف ر غ B005`; `ش ر ح B004 ↔ ذ ك ر B001`), zor doğum ve hayvan verimliliği (`ع س ر B007 ↔ ي س ر B006`; `ي س ر B006 ↔ ر ب ب B009`) için yerel tetikleyici yoktur.
- Ritüel kurban ve kumar okları (`ي س ر B007 ↔ ن ص ب B002`), savaş (`و ز ر B003 ↔ ن ص ب B008`) ve rekabetçi tahakküm (`و ز ر B006 ↔ ظ ه ر B007`) terfi ettirilmez.
- Göç/yolculuk (`ص د ر B003 ↔ ر ف ع B011`), gramer (`ر ف ع B012 ↔ ن ص ب B007`), özel adlar (`ع س ر B012 ↔ ي س ر B010`) ile yiyecek, tekstil, bitki, otlak ve hayvan hareketi kümeleri mekanik rezervuarda kalır.

## Açık sorular

1. İki kez tekrarlanan `مَعَ ٱلْعُسْرِ يُسْرًا`da “beraberlik”, eşzamanlı süreç mi, zorluk alanındaki kullanılabilir imkân mı, yoksa retorik güvence mi olarak öncelenmelidir?
2. `وِزْرَكَ`ın niteliği belirtilmediği için yükün görev, kaygı, tarihsel baskı veya başka bir içerikle özdeşleştirilmesinden kaçınmak gerekir. `ظ ه ر B013`teki utanç/kınama kalkışı `C/B` düzeyinde bile yükü “suç”a fazla yaklaştırıyor mu?
3. `ر ف ع B005/B010` ve `ذ ك ر B004`ün ses/tanıklık okumasında konuşan özne kimdir? Metin, muhatabın sesi ile onun başkalarınca anılmasını ayırmaya izin veriyor mu?
4. `ش ر ح B005` ile `ر غ ب B001` arasındaki güçlü yapısal bağ, genişletilen göğsün esas işlevini “arzu kapasitesi” diye daraltma riski taşıyor mu; açıklık, bilgi ve dayanma kapasitesi nasıl dengelenmeli?
5. `ع س ر B002`, `ي س ر B003`, `ظ ه ر B023`, `ن ص ب B005` ve `ر غ ب B004`ün ekonomik kümesi yerel bağlamca ne ölçüde denetleniyor? `C/B` üstüne çıkması için maddî paylaşımı gösteren hangi sûre-içi işaret gerekli olurdu?
6. `فَإِذَا فَرَغْتَ فَٱنصَبْ`, birbirini izleyen belirli görevleri mi, yoksa her tamamlanmayı yeni adanmış emeğe çeviren genel bir ritmi mi kurar?
7. `ن ص ب B004`teki yorgunluk ile yükün kaldırılması arasında sınır nasıl çizilmelidir? Sûre ezici yükü kaldırıp her emeği mi onaylar, yoksa yalnız Rabbe yönelmiş, taşıma kapasitesini yıkmayan emeği mi?
8. `و ز ر B004`, `ظ ه ر B006/B016` ve `ر ب ب B011`in destek ağı, ilahî yardımı toplumsal yardımla ilişkilendirmek için yeterli yerel kanıta sahip mi; yoksa bireysel rehabilitasyon ana okumada korunmalı mı?
9. Kaynakta `S` olarak işaretlenen `ع س ر B013`, `ي س ر B010` ve `ي س ر B011` dallarının etiket semantiği sonraki entegrasyonlarda açık bir sözleşmeyle tanımlanmalı mı?
10. Besmele analiz kapsamına dahil olduğu hâlde envanter 1. ayette başladığından rahmet yalnız çerçeve olarak kalıyor. Besmele kökleri için kaynak-temelli branch portları sağlanması grafı nasıl değiştirirdi?

## Sonuç

S94:1–8, rahatlamayı eylemsizlik değil kapasite onarımı olarak anlatır. Göğüs genişletilir, sırtı gıcırdatan yük indirilir, şerefli anılış yükseltilir ve bu geçmiş fiiller zorlukla beraber bulunan kolaylığın somut kanıtına dönüşür. Kolaylık, zorluğu inkâr eden dışsal bir ödül değil; onun içinde hareket, bitiriş ve yeniden başlama imkânıdır. Bu yüzden tamamlanma yeni emeğe, emek de Rabbe yönelmiş arzuya bağlanır. İkincil okumaların en güçlü katkısı, bu çevrimin ilişkisel ve kamusal boyutunu açmasıdır: yük paylaşılabilir, onarılan değer tanıklık olarak dolaşabilir, açılan imkân başkasına fayda olabilir ve serbest kalan kapasite koruyucu bir güven ilişkisi içinde yeniden görevlendirilebilir.
