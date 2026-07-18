# S95:1–8 (et-Tîn) — Nihai Bütünleştirme Raporu

## Kapsam ve yöntem notu

Bu rapor yalnız S95:1–8 için sağlanan `00-surah-text.json`, `01-passage.json`, `02-branches.json`, `03-candidate-bridges.json`, `05-activation-pass.json`, `06-mechanism.md`, `07-secondary-expansion.json`, `08-graph.json` ve `10-discovery-ranking.json` girdilerini bütünleştirir. QAC kelime sırası, morfoloji ve kök çözümlemesinde; `00-surah-text.json` tilavet metninde esas alınmıştır. Besmele analiz çerçevesine dahildir; fakat branch envanteri 1. ayetle başladığından Besmele’ye mahsus yeni kök veya branch kimliği üretilmemiştir. Yirmi iki kökün tamamı `resolved` durumundadır; eksik ya da dışarıda bırakılmış kök yoktur.

> بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ  
> وَٱلتِّينِ وَٱلزَّيْتُونِ  
> وَطُورِ سِينِينَ  
> وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ  
> لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ  
> ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ  
> إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ  
> فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ  
> أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ

## Kısa nihai rapor

Besmelenin rahmet çerçevesinden sonra yemin, iki şahit kümesi toplar. İncir ve zeytin, yüzeyde gerçek meyvelerdir (`ت ي ن B001`; `ز ي ت B002`) ve ekim, beslenme, yağ ile rızık alanını açar (`ز ي ت B001/B004`). Sina, adlandırılmış dağdır (`ط و ر B005`); güvenli şehir ise sınırları belli, emniyetli yurttur (`ب ل د B001`; `ء م ن B001`). Böylece insan hakkındaki iddia, hem hayatı besleyen yaratılmış düzenin hem de vahiy tarihini taşıyan kutsal mekânların şahitliği altında kurulur.

Yeminin ana iddiası, insanın tesadüfen değil ölçülerek ve dengelenerek yaratıldığıdır (`خ ل ق B001/B002/B003`; `ء ن س B001`). `أَحْسَنِ تَقْوِيمٍ`, yalnız güzel görünüş değil; güzellik ve mükemmellik (`ح س ن B001`), dik duruş, denge ve orantılı yapı (`ق و م B002/B008/B011/B015`) demektir. İkincil dallar bu kıvamı toplumsallık, niyet, sorumluluk ve iyi eylem kapasitesiyle genişletir (`ء ن س B003`; `ح س ن B002`; `ق و م B003`). İnsan “iyi biçimli” olduğu kadar iyiyi gerçekleştirmeye elverişli bir varlıktır.

Beşinci ayette bu yüksek konum tersine çevrilir: insan aşağıların aşağısına geri döndürülür (`ر د د B001`; `س ف ل B001/B002/B004`). `ثُمَّ`, dönüşü yaratılışın bir ayrıntısı değil, ondan sonra gelen yeni bir evre yapar. İkincil alan; bedensel yaşlanma ve işlev kaybı (`ق و م B016`; `ر د د B008`), yapısal dayanağın zayıflaması ve imandan geri dönüş (`ر د د B005`) gibi paralel gerçekleşmeleri korur. Bunların hiçbiri tek başına `أَسْفَلَ سَافِلِينَ`i tüketmez; ortak nokta, başlangıçtaki dik ve dengeli kıvamın artık gerçekleştirilememesidir.

Altıncı ayet bu inişi zorunlu ve tek sonuç olmaktan çıkaran istisnadır. İman, kalbe yerleşen güven ve tasdiktir (`ء م ن B002`); amel, niyetli eylemdir (`ع م ل B001`); `الصَّالِحَات` ise eylemi sağlam, doğru, yararlı ve onarıcı olmakla sınırlar (`ص ل ح B001/B002/B003`). Dolayısıyla istisna yalnız bir kimlik etiketi değildir. Yaratılışta verilmiş dik durma ve niyet kapasitesi, iman ve salih amelle korunur, toplumsal olarak gerçekleştirilir ve bozulmaya karşı onarılır.

Bu kişilere verilen `أَجْر`, doğrudan karşılık ve ödüldür (`ء ج ر B001`); fakat `غَيْرُ مَمْنُونٍ` onun kesilmesini veya azaltılmasını reddeder (`غ ي ر B005`; `م ن ن B001`). İkincil dallar, nimeti başa kakmayı (`م ن ن B003`) ve sonlu bir ücret hesabını da sınırlar; ücretsiz salıverme (`م ن ن B004`) ve sürdürücü güç (`م ن ن B002`) ödülün lütuf boyutunu açar. Böylece ödül, yalnız iş karşılığı ödenip kapanan ücret değil; insan kıvamını çöküşün ötesinde ayakta tutan, tükenmeyen ve aşağılamayan ihsandır.

Son iki soru sûrenin mantıksal sonucunu açığa çıkarır. Yaratılışın ölçüsü, aşağı dönüş ihtimali, iman–amel istisnası ve kesintisiz karşılık gösterildikten sonra hesap ve karşılığı yalanlamak tutarsızlaşır (`ك ذ ب B001/B002`; `ب ع د B002`; `د ي ن B002`). Son soru Allah’ı (`ء ل ه B001`) hükmedenlerin en hikmetlisi ve en adili olarak tanımlar (`ح ك م B002/B003`). İnsanı ölçüyle biçimlendiren kudretin, o biçimin nasıl kullanıldığını değerlendirmeye de yetkin olması sûrenin yaratılış ile hüküm arasındaki temel bağıdır.

Hüküm, yaratılışa dışarıdan eklenmiş yabancı bir mahkeme değildir. `ح ك م B001/B003/B004`, yanlışı sınırlama, hakikate ulaşan hikmet ve şeyi sağlam biçimde tamamlama anlamlarını taşır. Bu dallar `خ ل ق B003` ve `ق و م B008` ile birleştiğinde son yargı, yaratılıştaki bilge düzenin açığa çıkarılması ve bozulmuş olanın adaletle ayrıştırılması olur. Yaratıcının biçim verme yetkinliği, Hâkimin değerlendirme yetkinliğinin delilidir.

Birincil mekanizma özetle şöyledir: **rahmet çerçevesi → besleyici ve kutsal şahitler → en güzel insan kıvamı → aşağı dönüş → iman ve salih amel istisnası → kesintisiz karşılık → kaçınılmaz ve kusursuz ilahî hüküm**. Sûrenin insan onuru öğretisi, insanın otomatik olarak hep yüksek kalacağını söylemez; ona yüksek bir başlangıç, gerçek bir düşüş ihtimali, eylem sorumluluğu ve adil nihai karşılık verir.

### Yorum sınırları

- `A`, yüzey ve yakın bağlamın doğrudan taşıdığı; `B`, güçlü ikincil; `C/B`, kontrollü fakat ihtiyatlı latent; `C`, geniş keşif rezervuarında korunan fakat yerel mekanizmaya alınmayan etikettir.
- İkincil okumalar yüzey anlamını değiştirmez: incir ve zeytin yalnız yer adına, `أَجْر` kemik onarımına, `دِين` borca veya `مَمْنُون` ölçülmüş ağırlığa indirgenmez.
- `10-discovery-ranking.json`, 4.146 aday arasından sürpriz değeri yüksek mekanik bir inceleme kuyruğudur; yorum hükmü değildir. Seçicilik yalnız “Most surprising discoveries” bölümünde uygulanır.

## Aktive edilmiş branch tablosu

Envanter muhasebesi: **22 kök, 166 branch; A=24, B=35, C/B=29, C=78.** Aşağıdaki tablo `05-activation-pass.json` içindeki bütün branch rezervuarını seçmeden korur.

| Kök | Branch’ler ve aktivasyon rolleri |
|---|---|
| ت ي ن | `B001 [A]` yeminde anılan yenilebilir incir; `B002 [B]` incirle ilişkili dağ veya kutsal yer; `B003 [C]` Tinan adlı kurt. |
| ز ي ت | `B001 [B]` zeytinyağı ve çıkarılmış besin; `B002 [A]` yemindeki zeytin ağacı veya meyvesi; `B003 [C/B]` yağla mesh etme veya bakım; `B004 [B]` yiyecek, rızık ve armağan olarak yağ; `B005 [C]` yağ satıcısı veya sıkıcısı. |
| ط و ر | `B001 [C]` yapının yanında uzanan kenar veya çevre; `B002 [C]` korunan sınıra yakınlık; `B003 [C/B]` aşılmaması gereken sınır; `B004 [B]` gelişimin ardışık evre ve hâlleri; `B005 [A]` adlandırılmış Sina Dağı; `B006 [C]` insanî toplumsallığın dışındaki yabanilik; `B007 [C]` bir yerde hiç kimsenin bulunmaması. |
| ب ل د | `B001 [A]` yeminde anılan sınırlı ülke veya şehir; `B002 [C]` göğüs anatomisi; `B003 [C]` kaşlar arasındaki belirgin işaret; `B004 [C]` ay konağı veya boş göksel yer; `B005 [C]` şaşkınlık ve zihinsel donukluk; `B006 [C]` deri ve bedendeki iz; `B007 [C]` donukluk ve zayıf performans; `B008 [C/B]` kalın yapı ve iri beden; `B009 [B]` şehirde yaşama ve oraya ait olma; `B010 [C/B]` yere bastırma veya yapışma; `B011 [C]` kılıç veya sopayla dövüşme; `B012 [C]` devekuşu yuva çukuru. |
| ء م ن | `B001 [A]` şehrin güvenliği ve güvenilir barışı; `B002 [A]` kalbe yerleşen iman ve tasdik; `B003 [C/B]` litürjik Âmin ve cevap talebi. |
| خ ل ق | `B001 [B]` biçimlendirmeden önce ölçme ve oranlama; `B002 [A]` ilahî yaratma ve var etme; `B003 [B]` tam oluşum ve dengeli görünür biçim; `B004 [C/B]` içsel yatkınlık ve ahlâkî karakter; `B005 [C]` işe uygunluk ve hazır oluş; `B006 [B]` hayırdan veya âhiretten ayrılmış pay; `B007 [C/B]` yalan veya söylem uydurma; `B008 [C]` pürüzsüz ve düz yüzey; `B009 [C]` yıpranmış giysi ve maddî bozulma; `B010 [C]` kokulu bedensel yağlama; `B011 [C]` su tutan kaya oyuğu veya kuyu; `B012 [C]` kaya gibi katı kapanış. |
| ء ن س | `B001 [A]` yabanilik ve cinlerden ayrı insan; `B002 [C]` görme, işitme veya duyuyla algılama; `B003 [B]` yabancılığı gideren toplumsallık ve yoldaşlık; `B004 [C]` insana dönük taraf ve bedensel yönelim; `B005 [C]` göz bebeğine yansıyan insan imgesi; `B006 [C/B]` benlik, yakın yoldaş ve seçilmiş akraba; `B007 [C]` evlere girmeden izin isteme. |
| ح س ن | `B001 [A]` çirkinliğin karşıtı güzellik ve mükemmellik; `B002 [B]` iyiliği ihsan ve mükemmellikle yapma; `B003 [B]` nimet, ödül veya sonuç olarak alınan iyilik; `B004 [C]` yer veya beden için güzellikten türeyen özel adlar; `B005 [C/B]` azamî çaba, sınır veya en iyi derece. |
| ق و م | `B001 [C/B]` insan topluluğu ve cemaat; `B002 [B]` bedenin dik duruşu; `B003 [B]` işe azimle kalkma; `B004 [C/B]` sürdürme, koruma ve yönetme; `B005 [C/B]` yükümlülüğü kurma ve yerine getirme; `B006 [C]` makam veya yerleşik ikamet; `B007 [C]` başkasının yerine geçme; `B008 [A]` diklik, denge ve mükemmel oluşum; `B009 [B]` hayatı ayakta tutan destek, yapı ve araç; `B010 [C]` değer biçme ve fiyatlandırma; `B011 [B]` beden boyu ve oranlı yükseklik; `B012 [C]` dik araç veya destek parçası; `B013 [B]` diriliş ve hüküm için ayağa kalkma; `B014 [C]` direnme ve çatışma; `B015 [C/B]` dengeli ağırlık ve eşit ölçü; `B016 [B]` durma, yorgunluk ve bozuk hareket; `B017 [C]` öğle ve zamansal orta nokta; `B018 [C]` canlı pazar; `B019 [C]` organdaki kalıcı ağrı; `B020 [C]` hayvan bacağı hastalığı; `B021 [C]` sağlam görünüp görmeyen göz. |
| ر د د | `B001 [A]` kişiyi önceki veya değişmiş hâle döndürme; `B002 [C/B]` geri çevirme, itme veya engelleme; `B003 [C/B]` yanlış veya kabul edilmezi reddetme; `B004 [C]` değişimde iade veya fesih; `B005 [C/B]` irtidat ve imandan geri dönüş; `B006 [C]` boşanmış kadının ailesine dönmesi; `B007 [C]` dolu meme veya toplanmış su; `B008 [C/B]` görme, konuşma veya görünüşü bozan kusur; `B009 [C]` çökmeyi engelleyen destek; `B010 [C/B]` tekrar, salınım ve tereddüt. |
| س ف ل | `B001 [A]` yukarının altındaki en aşağı mekân; `B002 [A]` en düşük derece ve alçalmış insan hâli; `B003 [C]` rüzgâr-altı veya aşağı rüzgâr yönü; `B004 [B]` aşağı indirme veya aşağı hareket; `B005 [C]` devenin alt destek bacakları; `B006 [C/B]` alt nesil olarak genç/yavru hayvan; `B007 [C]` bedenin alt bölgesi. |
| ع م ل | `B001 [A]` niyetli eylem, özellikle salih ameller; `B002 [C]` bir şeyi işletme veya kullanma; `B003 [C]` makam yürütme ve idare; `B004 [B]` çalışmayla kazanılan ücret ve geçim; `B005 [C/B]` insanlar arasında karşılıklı muamele; `B006 [C]` el işçileri; `B007 [C]` zahmet ve yük; `B008 [C]` işe doğuştan uygun mizaç; `B009 [C]` mızrağın işleyen bölümü; `B010 [C]` çalışan uzuv veya organ; `B011 [C]` çok kullanılan yol; `B012 [C]` yaya yolcular. |
| ص ل ح | `B001 [A]` bozulmanın karşıtı doğruluk ve sağlamlık; `B002 [B]` uzlaşma ve toplumsal yabancılığın kaldırılması; `B003 [B]` uygunluk, elverişlilik ve yararlı işlev; `B004 [C]` Salih veya ilişkili kişi adları; `B005 [C]` Salah ya da es-Sulh yer adları. |
| ء ج ر | `B001 [A]` işin karşılığı ve ödül; `B002 [C/B]` kusur kalsa bile kırığı onarma; `B003 [C]` korumasız çatı. |
| غ ي ر | `B001 [B]` fayda, rızık, sulama ve onarım; `B002 [C]` diyet/tazminat; `B003 [B]` biçim değişikliği veya ikame; `B004 [C]` yakınları koruyan kıskançlık; `B005 [A]` başkalık, dışlama ve olumsuzlama. |
| م ن ن | `B001 [A]` süren ödülü kesme veya azaltma; `B002 [C/B]` şeyi ayakta tutan kuvvet veya onun kaybı; `B003 [B]` ihsan veya nimeti başa kakma; `B004 [C/B]` karşılıksız serbest bırakma; `B005 [C]` menn adlı ölçülü ağırlık; `B006 [C/B]` rızık olarak inen tatlı kudret helvası. |
| ك ذ ب | `B001 [B]` hakikatin karşıtı yalan; `B002 [A]` yalan isnat etme ve hükmü inkâr; `B003 [C]` eyleme teşvik veya yükümlülük deyimi; `B004 [C]` tökezleme veya suçlamada doğru çıkma; `B005 [C/B]` eylem öncesi gecikmeme/oyalanmama; `B006 [C]` sütün devam etmeyip kesilmesi; `B007 [C]` yaban hayvanının koşup geriye bakmak için durması; `B008 [B]` aldatıcı benlik veya içsel yalancı karakter; `B009 [C]` görünüşü aldatan giysi. |
| ب ع د | `B001 [C/B]` yakınlığın karşıtı uzaklık; `B002 [A]` zamansal sonralık ve ardışıklık; `B003 [C]` uzaklaştırma veya ayırma; `B004 [B]` mahvolma, dışlanma veya lanet; `B005 [C]` yakın akrabanın karşıtı uzak akraba; `B006 [C]` uzak/aşağı olmayan deyimi; `B007 [C]` ayrı aralıklarla tekrarlanan olaylar; `B008 [B]` derinlik ve ileri görüşlü sağlam hüküm; `B009 [C]` fayda veya değer yokluğu; `B010 [C]` düşmanlıkta ileri gitme. |
| د ي ن | `B001 [B]` dinî teslimiyet ve itaat; `B002 [A]` hüküm, hesap ve karşılık; `B003 [C]` malî borç ve ertelenmiş yükümlülük; `B004 [C/B]` egemenlik, boyun eğdirme ve zorlayıcı güç; `B005 [C]` alışılmış uygulama ve düzen; `B006 [C]` otorite altında örgütlenmiş şehir; `B007 [B]` doğrulama, emanet ve tanıklığı kabul. |
| ل ي س | `B001 [A]` nakıs fiille ifade edilen retorik olumsuzlama; `B002 [C]` adlandırılmış unsuru dışlayan istisna; `B003 [B]` `lā` gibi işleyen olumsuzlama; `B004 [C]` korkusuz savaşçı; `B005 [C]` bir yere bağlı kalan kişi; `B006 [C]` tahammül ve iyi mizaç; `B007 [C]` hüküm zayıflığı; `B008 [C]` koruyucu kıskançlık yokluğunun kınanması. |
| ء ل ه | `B001 [A]` ibadet edilen ilah ve egemen olarak Allah; `B002 [B]` ciddi formül ve hitapta ilahî isim. |
| ح ك م | `B001 [B]` yanlışı sınırlama ve düzeni geri getirme; `B002 [A]` insanlar arasında adaletle hükmetme; `B003 [B]` hakikate ulaşan hikmet ve bilgi; `B004 [B]` sağlamlaştırma, güvenceye alma ve iyi biçimlendirme; `B005 [C/B]` hükmü emanet etme veya yetki devri; `B006 [C]` hayvanı sınırlayan gem; `B007 [C/B]` geri çevirme veya dönüşe sebep olma. |

## İkincil aktivasyon tablosu

Bu tablo `07-secondary-expansion.json` içindeki 25 yeni veya güçlendirilmiş adayı gösterir. Değişmeyen etiketler, yerel gerekçesi ikincil geçişte ayrıca pekiştirilen branch’lerdir.

| Kök / branch | Geçiş | İkincil katkı ve sınır |
|---|---:|---|
| `ء م ن B003` | `C/B → C/B` | Besmele, yemin ve Allah adını içeren kapanış altında dua–cevap/Âmin kaydını korur; metinde `آمين` yoktur. |
| `ء ل ه B002` | `B → B` | Zirve sorusundaki Allah adını ciddi hitap, tasdik ve nihai kabulle bağlar; özel adı gramatik formüle indirgemez. |
| `ق و م B013` | `B → B` | En güzel dik kıvamı, hesap için yeniden ayağa kalkışla tamamlar; yaratılmış duruştan nihai değerlendirme duruşuna geçer. |
| `د ي ن B007` | `B → B` | Yaratılış, düşüş, iman, amel ve ödül kanıtlarından sonra hesap için doğrulama, güvenilir tanıklık ve vicdan adımını kurar. |
| `ح ك م B005` | `C/B → B` | Son retorik soru, hükmü en üstün Hâkime emanet etmeye ve kararını kabule çağırır; insanî tahkim usulü anlatmaz. |
| `ب ع د B008` | `B → B` | Tamamlanmış kanıt dizisinin ardından ileri görüşlü ve derin hükmü olumlu muhakeme standardı yapar. |
| `ل ي س B007` | `C → C/B` | Zayıf hükmü, `أَحْكَمِ الْحَاكِمِينَ` karşısında eksik insan değerlendirmesinin kontrollü karşı kutbu yapar; yüzey anlam olumsuzlamadır. |
| `ل ي س B002` | `C → B` | İman–amel istisnası, ödülden sonluluğun dışlanması ve son olumsuz soru arasındaki küme üyeliği/dışlama mantığını görünür kılar. |
| `ل ي س B003` | `B → B` | Kategorik olumsuzlama; istisnanın korunması, ödülün sonluluğunun reddi ve ilahî hükümden kusurun dışlanmasını biçimselleştirir. |
| `غ ي ر B003` | `B → B` | Güzel kıvamdan aşağı hâle ve korunmuş sonuca geçişte biçim değişikliğini yapısal düzeyde açıklar; 6. ayetteki `غير` “dönüşüm” demek değildir. |
| `خ ل ق B004` | `C/B → B` | En güzel kıvamın iman, amel, inkâr ve ahlâkî değişime açık içsel karakter boyutunu güçlendirir; yaratılışta sabit ahlâkî kader iddia etmez. |
| `ك ذ ب B008` | `B → B` | İnkârı yalnız yanlış önermeye değil, yaratılmış ahlâkî kapasiteyi boşa çıkaran aldatıcı benliğe bağlar. |
| `ح ك م B007` | `C/B → B` | Kusursuz hükmün düşüş yörüngesini düzene doğru geri çevirebilen onarıcı boyutunu açar; ceza ve değerlendirmeyi silmez. |
| `ر د د B009` | `C → B` | Aşağı dönüşün yapısal çöküşüne karşı destek portu açar; iman–salih amel istisnasını ayakta kalma/onarılma olarak okur, literal payanda yoktur. |
| `م ن ن B002` | `C/B → B` | Kesilmeyen ödülü, varlığı ayakta tutan ve tükenmeyen sürdürücü kuvvet olarak derinleştirir. |
| `ء ج ر B002` | `C/B → B` | Ödüle, bozulmuş veya kırılmış formu onarma gölgesi ekler; kemikçilik ve beden yaralanması yüzey anlamı değildir. |
| `ق و م B009` | `B → B` | Hayatı ve yapıyı ayakta tutan desteği, güzel kıvamın iman ve salih amelle korunmasına bağlar; geçim tek destek biçimi değildir. |
| `م ن ن B004` | `C/B → B` | İş–ücret–borç–hesap alanına karşı, karşılıksız özgür bırakma/lütuf kutbunu güçlendirir; savaş, esaret ve fidye ayrıntıları alınmaz. |
| `ز ي ت B003` | `C/B → C/B` | Zeytinyağının bedene uygulanmasını, yaratılmış bedene bakım ve şeref analoğu yapar; literal ritüel veya hijyen eylemi yoktur. |
| `خ ل ق B010` | `C → C/B` | Kokulu bedensel bakımı zeytinle birleştirerek güzel yaratılışa onurlandırılmış beden analoğu ekler; parfüm/kozmetik yüzey olayı değildir. |
| `خ ل ق B009` | `C → C/B` | Yıpranan giysiyi, iyi başlangıçtan sonra formun bütünlüğünü kaybetmesinin maddî imgesi yapar; tekstil anlatılmaz. |
| `ك ذ ب B009` | `C → C/B` | Aldatıcı giysiyi, dış görünüşün içsel hakikati yanlış sunabilmesinin kontrollü görsel analoğu yapar. |
| `ق و م B015` | `C/B → B` | Dengeli ölçüyü `تَقْوِيم` ve hesap arasında metrolojik köprü yapar; kesintisiz ödül bunu kapalı hakediş denklemine dönüşmekten alıkoyar. |
| `م ن ن B005` | `C → C/B` | Ölçülü `menn` ağırlığı, kıvam–iş–ödül–hesap alanına muhasebe dili ekler; bağlam ödülü sonlu tartılmış miktara indirgemez. |
| `د ي ن B003` | `C → C/B` | Borç ve ertelenmiş yükümlülüğü amel–karşılık–sonraki hesap için sonlu ekonomik model yapar; sûre modeli kesintisiz lütufla aşar. |

### İkincil mekanizma kümeleri

1. **oath_becomes_prayer_and_answer — `C/B`:** `ت ي ن → ز ي ت → ط و ر → ب ل د → ء م ن → ء ل ه → ح ك م`. Besleyici ve kutsal şahitler ciddi bir hitap kurar; güven imana, formülsel tasdik cevaba ve ilahî ad kusursuz hükmün kabulüne uzanır. Âmin lafzı metinde yoktur.
2. **exception_logic_structures_moral_outcome — `B`:** `غ ي ر → ل ي س → ء م ن → ع م ل → ص ل ح → م ن ن`. İman edip salih amel işleyenler düşüşten ayrılır; sonluluk ve başa kakma ödülden, kusur ise ilahî hükümden dışlanır.
3. **inner_form_confronts_the_deceptive_self — `B`:** `خ ل ق → ء ن س → ح س ن → ك ذ ب → ر د د → س ف ل`. Güzel form içsel karakter ve toplumsal fail olma kapasitesi taşır; aldatıcı benlik bu kapasiteyi inkâr ve geri dönüşle boşa çıkarabilir.
4. **judgment_as_entrusted_verification — `B`:** `ء م ن → ك ذ ب → ب ع د → د ي ن → ل ي س → ح ك م`. İşaretler inkâr değil doğrulama ister; derin muhakeme kanıtı tanır ve nihai karar hakikate ulaşan Hâkime emanet edilir.
5. **reward_repairs_and_sustains_form — `B`:** `ر د د → ق و م → ص ل ح → ء ج ر → م ن ن → ح ك م`. Düşüş iyi formu zedeler; salih eylem onarıcıdır, ödül kırık onarımı gölgesi ve sürdürücü güç taşır, hüküm yörüngeyi düzene çevirebilir.
6. **measured_economy_exceeded_by_grace — `B`:** `ق و م → ع م ل → ء ج ر → د ي ن → م ن ن → غ ي ر`. Ölçülü yaratılış, ücretli iş, karşılık, borç ve hesap bir muhasebe alanı kurar; kesilmeyen, başa kakılmayan ve karşılıksız lütuf bu kapalı hesabı aşar.
7. **embodied_dignity_anointed_not_consumed — `C/B`:** `ز ي ت → خ ل ق → ء ن س → ح س ن → ق و م`. Zeytin yalnız beslemez; yağ olarak bedene bakım ve onur analoğu verir. Ritüel uygulama iddia edilmez.
8. **worn_appearance_versus_enduring_truth — `C/B`:** `خ ل ق → ك ذ ب → غ ي ر → ر د د → ص ل ح → م ن ن`. Form yıpranabilir, görünüş aldatabilir ve dönüş kusur getirebilir; sağlam eylem ve azalmayan ödül kalıcı hakikati sahte yüzeyden ayırır.

## Graph-ready kök/düğüm ve kenar açıklaması

### Düğüm ve port semantiği

- **Düğüm türü:** yalnız kök (`type=root`).
- **Düğüm kümesi (22):** `ت ي ن`, `ز ي ت`, `ط و ر`, `ب ل د`, `ء م ن`, `خ ل ق`, `ء ن س`, `ح س ن`, `ق و م`, `ر د د`, `س ف ل`, `ع م ل`, `ص ل ح`, `ء ج ر`, `غ ي ر`, `م ن ن`, `ك ذ ب`, `ب ع د`, `د ي ن`, `ل ي س`, `ء ل ه`, `ح ك م`.
- **Portlar:** branch kimlikleri düğüm değil, kenarların kaynak/hedef kanıt etiketleridir.
- **Ok yönü:** anlatısal veya mekanizma yönüdür; sözlüksel/ontolojik nedensellik iddiası değildir.

### Birincil ve güçlü latent kenarlar

```text
ت ي ن -> ز ي ت | ت ي ن B001 :: ز ي ت B002/B001/B004 | ekili meyve, beslenme ve rızık şahidi | active/latent
ت ي ن -> ط و ر | ت ي ن B002 :: ط و ر B005 | ikincil incir-kutsal yer portu ile Sina | latent
ط و ر -> ب ل د | ط و ر B005 :: ب ل د B001 | adlandırılmış dağ ve güvenli şehirden kutsal coğrafya | active
ب ل د -> ء م ن | ب ل د B001 :: ء م ن B001 | sınırlı şehrin güvenilir emniyeti | active
خ ل ق -> ق و م | خ ل ق B001/B003 :: ق و م B002/B008/B011/B015 | ölçme, dengeli biçim, diklik ve orantı | active/latent
خ ل ق -> ء ن س | خ ل ق B002 :: ء ن س B001/B003 | yaratmanın nesnesi olarak bedensel ve toplumsal insan | active/latent
ح س ن -> ق و م | ح س ن B001/B002 :: ق و م B008/B003 | mükemmel kıvamın iyi eylem kapasitesine açılması | active/latent
ح س ن -> ر د د | ح س ن B001 :: ر د د B008 | en iyi form ile sonradan oluşan kusur karşıtlığı | active/latent
ر د د -> س ف ل | ر د د B001 :: س ف ل B001/B002/B004 | aşağı ve alçalmış hâle yöneltilmiş dönüş | active
ق و م -> ع م ل | ق و م B003 :: ع م ل B001 | dik duruş ve azmin niyetli eyleme dönüşmesi | active/latent
ع م ل -> ص ل ح | ع م ل B001 :: ص ل ح B001/B002/B003 | eylemin sağlam, uygun ve onarıcı olması | active/latent
ء م ن -> ك ذ ب | ء م ن B002 :: ك ذ ب B001/B002 | yerleşik tasdik ile yalanlama karşıtlığı | active
ع م ل -> ء ج ر | ع م ل B001/B004 :: ء ج ر B001 | salih iş ve karşılık | active/latent
غ ي ر -> م ن ن | غ ي ر B005 :: م ن ن B001/B003/B004 | ödülden kesilme, azalma ve başa kakmanın dışlanması | active/latent
ص ل ح -> ح ك م | ص ل ح B001 :: ح ك م B001 | sağlamlık/onarımdan düzeni geri getiren hükme | active/latent
ق و م -> د ي ن | ق و م B013 :: د ي ن B002 | yaratılmış diklikten hesap için ayağa kalkışa | latent
د ي ن -> ح ك م | د ي ن B002 :: ح ك م B002/B003 | hesap ve karşılıktan adil, hakikate ulaşan hükme | active/latent
خ ل ق -> ح ك م | خ ل ق B003 :: ح ك م B004 | tam biçim ile kusursuz düzenleyici hüküm | active/latent
ء ل ه -> ح ك م | ء ل ه B001 :: ح ك م B002 | Allah’ın en üstün Hâkim olarak mekanizmayı kapatması | active
```

### Keşif düzeyi kenarlar

```text
ق و م -> م ن ن | ق و م B015 :: م ن ن B005 | dengeli ölçü ile ölçülü ağırlık; muhasebe alt-katmanı | C/B
ع م ل -> د ي ن | ع م ل B004 :: د ي ن B003 | ücretli iş ile ertelenmiş borç/yükümlülük | C/B
ء ج ر -> د ي ن | ء ج ر B001 :: د ي ن B003 | karşılık ile ekonomik yükümlülük; hüküm anlamı birincil | C/B
ص ل ح -> ء ج ر | ص ل ح B001 :: ء ج ر B002 | sağlamlık ve reform ile kırık onarımının ödül gölgesi | B
ر د د -> م ن ن | ر د د B009 :: م ن ن B002 | çökmeyi önleyen destek ile sürdürücü kuvvet | B
ز ي ت -> خ ل ق | ز ي ت B003 :: خ ل ق B010 | yağla bakım ile yaratılmış bedene kokulu bakım | C/B
خ ل ق -> ك ذ ب | خ ل ق B009 :: ك ذ ب B009 | yıpranmış biçim ile aldatıcı dış görünüş | C/B
```

### Mekanik olarak güçlü fakat yerel olarak etkinleştirilmemiş kümeler

```text
ر د د B006 :: غ ي ر B004 / ب ع د B005 | evlilik, cinsiyet ve uzak akrabalık | C
ء ن س B002 :: ك ذ ب B007 | hayvanın durup geri bakmasıyla algı/dikkat | C
ب ل د B010 :: خ ل ق B011 | yer, kap ve su tutma ortaklığı | C
ز ي ت B003 :: ب ل د B002 | yağ ve göğüs anatomisi | C
ء ن س B006 :: ل ي س B008 | akrabalık ve cinsellik | C
ب ل د B011 :: ق و م B014 | savaş, güç ve çatışma | C
```

## Most surprising discoveries

### 1. Ölçülü yaratılış bir muhasebe alanı kuruyor, fakat lütuf hesabı aşıyor

En tutarlı sürpriz, metrolojik-ekonomik kümedir. `ق و م B015 ↔ م ن ن B005`, `تَقْوِيم`deki dengeli ölçüyü `menn` adlı tartı birimiyle bağlar. `ع م ل B004`, ücretli emeği; `ء ج ر B001`, karşılığı; `د ي ن B003`, ertelenmiş borcu devreye sokar. İnsan ölçülür, eylem yapılır ve karşılık hesaplanır gibi görünür. Fakat `غَيْرُ مَمْنُونٍ`, ödülün kesilmesini ve sonlu tartılmış bir hesaba kapanmasını reddeder; `م ن ن B004` karşılıksız lütuf kapısını açar. Keşif, “kurtuluş ticari sözleşmedir” değil, ölçü ve karşılık dilinin lütuf tarafından aşılmasıdır.

### 2. Ödül yalnız ödeme değil, kırılmış formun onarımı olabilir

`ء ج ر B002`, kusur kalsa bile kırığı onarma dalıdır. Bu dal, salihliğin sağlamlık/onarıcılığı (`ص ل ح B001`), iyi formdan sonra oluşan bozukluk (`ر د د B008`), çökmeyi önleyen destek (`ر د د B009`; `ق و م B009`) ve tükenmeyen kuvvetle (`م ن ن B002`) birleşir. Böylece `أَجْر`, doğrudan anlamı ödül kalmakla birlikte, düşüşte zedelenen insan kıvamını yeniden ayakta tutan bir onarım gölgesi kazanır. Literal kemikçilik veya yaralanma iddia edilmez.

### 3. En güzel “ayakta duruş”, hüküm için yeniden ayağa kalkışla tamamlanıyor

`ق و م B013 ↔ د ي ن B002`, yaratılıştaki dik ve dengeli duruşu diriliş ve hesap için ayağa kalkışla bağlar. İnsan yalnız başlangıçta biçim verilmiş bir beden değildir; verilen kıvamın nasıl kullanıldığının değerlendirileceği son duruşa da çağrılır. Bu kenar, yaratılış ile hüküm arasındaki mesafeyi kapatır: Aynı kök hem iyi formun ayakta oluşunu hem de o formun hesap önünde yeniden ayakta durmasını taşır.

### 4. Zeytin, besinden bedensel onura geçiyor

`ز ي ت B003 ↔ خ ل ق B010`, yağla mesh/bakımı kokulu bedensel uygulamayla birleştirir. Açılıştaki zeytin böylece yalnız yenilen ve enerji veren ürün değil, yaratılmış bedene bakım ve şeref gösterebilen madde olarak da belirir. Bu, sûrenin bedensel insan onuru temasını maddî olarak derinleştirir; fakat ayetlerde ritüel mesh, hijyen veya kozmetik eylemi yoktur ve okuma `C/B` kalır.

### 5. Yıpranmış biçim ile aldatıcı görünüş, düşüş ve inkâra görsel bir analog veriyor

`خ ل ق B009 ↔ ك ذ ب B009`, yıpranan giysiyi görünüşü aldatan giysiyle bağlar. Kontrollü bir metafor olarak bu küme, en iyi formdan aşağı hâle geçişi ve inkârın hakikati yanlış sunmasını kesiştirir: Yüzey bozulabilir, hatta iç durumu olduğundan farklı gösterebilir. Bağlam düşüşü ve hakikat sınamasını destekler, fakat giysi anlamlarını etkin yüzey okuması yapmaz.

### 6. Yemin, dua ve cevap kaydına yaklaşırken hükmün kabulüyle kapanıyor

`ء م ن B003 ↔ ء ل ه B002`, litürjik Âmin/cevap dalını ciddi ilahî ad ve hitapla bağlar. Besmele, yeminler, iman istisnası ve “Allah hâkimlerin en hikmetlisi değil midir?” sorusu birlikte, okuyucudan yalnız bilgi değil tasdik bekleyen bir söylem kurar. Metinde `آمين` sözcüğü bulunmadığından bu, recited text değil kontrollü bir dua–cevap alt-katmanıdır.

### Seçilmemiş fakat rezervuarda korunan yüksek-sürpriz adaylar

- `ر د د B006 ↔ غ ي ر B004` ve `ر د د B006 ↔ ب ع د B005` evlilik, cinsiyet ve akrabalık ortaklıklarıdır; pasajda yerel tetikleyici yoktur.
- `ء ن س B002 ↔ ك ذ ب B007`, algı/dikkati koşup geri bakan yaban hayvanıyla bağlar; insan, inkâr ve hüküm mekanizmasına yeterince yerleşmez.
- `ب ل د B010 ↔ خ ل ق B011` su tutan yer/kap; `ز ي ت B003 ↔ ب ل د B002` yağ ve göğüs anatomisi kümeleri mekanik kalır.
- Savaş ve çatışma (`ب ل د B011 ↔ ق و م B014`), akrabalık/cinsellik (`ء ن س B006 ↔ ل ي س B008`) ve izole hayvan, özel ad, arazi çağrışımları terfi ettirilmez.

## Açık sorular

1. Açılıştaki incir ve zeytin yalnız gerçek meyveler olarak mı tutulmalı, yoksa `ت ي ن B002` üzerinden Sina ve güvenli şehirle birlikte ikincil kutsal coğrafya kaydı ne ölçüde etkinleştirilmeli?
2. `أَحْسَنِ تَقْوِيمٍ`de `ق و م B008` birincil iken beden (`B002/B011`), ahlâkî kapasite (`خ ل ق B004`; `ح س ن B002`) ve toplumsallık (`ء ن س B003`) arasında hangi hiyerarşi kurulmalıdır?
3. `أَسْفَلَ سَافِلِينَ`in bedensel yaşlanma, işlev kaybı ve ahlâkî geri dönüş alt-okumaları aynı anda tutulabilir mi; biri öne alındığında diğerlerini susturma riski nedir?
4. İman ve salih amel istisnası, aşağı dönüşü tamamen engelliyor mu, yoksa bedensel düşüş sürerken insanın ahlâkî ve nihai ayakta kalışını mı koruyor?
5. `ء ج ر B002`, `ر د د B009`, `ق و م B009` ve `م ن ن B002`nin “ödül onarır ve ayakta tutar” mekanizması `B` için yeterince yerel mi; yoksa kırık onarımı ayrıntısı `C/B` kalmalı mı?
6. `ق و م B015`, `م ن ن B005`, `ع م ل B004`, `ء ج ر B001` ve `د ي ن B003`ün muhasebe kümesi, lütfun hesabı aşmasını göstermek için mi kullanışlıdır, yoksa metni gereğinden fazla ekonomikleştirir mi?
7. `غَيْرُ مَمْنُونٍ`de ana vurgu kesintisizlik (`م ن ن B001`), başa kakmama (`B003`), karşılıksız lütuf (`B004`) veya sürdürücü kuvvet (`B002`) arasında nasıl dağıtılmalıdır?
8. `ح ك م B007`nin onarıcı geri çevirme işlevi, nihai hükmün düzeni restore etmesini açıklarken cezalandırıcı ve ayırt edici boyutu gölgeliyor mu?
9. `ك ذ ب B008`teki “aldatıcı benlik”, inkârın iç mekanizmasını aydınlatıyor; ancak yalanlamayı psikolojik karaktere indirgeme riski nasıl sınırlandırılmalı?
10. Besmele kapsamda olduğu hâlde kök envanteri 1. ayetten başlıyor. Rahmet kökleri için kaynak-temelli branch portları sağlansaydı yaratılış–ödül–hüküm grafı nasıl değişirdi?

## Sonuç

S95:1–8, insan onurunu durağan bir üstünlük iddiası olarak değil, ölçülü yaratılış ile sorumlu sonuç arasındaki gerilim olarak kurar. Besleyici ürünler ve güvenli kutsal mekânlar, hayatın elverişli kılındığı bir dünyaya tanıklık eder; insan bu dünyada dik, dengeli, toplumsal ve eyleme yetkin biçimde yaratılır. Fakat bu kıvam aşağı dönüşe açıktır. İman ve salih amel, yaratılmış kapasiteyi doğru ve onarıcı kullanımda gerçekleştirir; kesilmeyen ödül bu formu düşüşün ötesinde ayakta tutar; kusursuz hüküm ise yaratılışta kurulmuş bilge düzeni adaletle değerlendirir. İkincil okumaların en güçlü katkısı, ödülü sonlu muhasebenin ötesine geçen onarım ve sürdürücü lütuf, hükmü ise yaratılmış düzenin tamamlanması olarak göstermesidir.
