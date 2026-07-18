# S98:5–6 Nihai Bütünleştirme Raporu

## Kapsam ve veri özeti

Bu rapor yalnız S98:5–6 pasajını ve bu paketin yetkili girdilerini bütünleştirir. QAC sırasına göre 18 kökün 17’si tekil olarak çözümlenmiş, `ب ر ء` ise `root_000099` ve `root_000100` kaynaklarından deterministik biçimde birleştirilmiştir; eksik veya dışarıda bırakılmış kök yoktur. Aktivasyon rezervuarında 169 dal bulunur: `A=27`, `B=35`, `C=72`, `C/B=34`, `S=1`. Kök grafiği 18 düğüm ve 4126 aday kenar içerir. Köprü incelemesinde yalnız 80 öğelik `03-candidate-bridges.agent.json` kuyruğu kullanılmış, tam rezervuar tüketilmemiştir. `10-discovery-ranking.json` salt okunur mekanik keşif sırası olarak korunmuştur.

## Kaynak metin

> بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ  
> وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ  
> إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ

## Kısa nihai rapor

Besmelenin rahmet çerçevesi altında 5. ayet birbirinden kopuk görevler değil, tek bir dinî bütünlük kurar. İlahî emir (`ء م ر B002`) Allah’a kulluk ve ibadete (`ع ب د B002/B003`, `ء ل ه B001/B002`) yönelir. İhlas (`خ ل ص B001/B005`), dini karışımdan ve ortaklıktan ayırır (`خ ل ص B004`); hanif yöneliş (`ح ن ف B002/B003`) bu arınmış bağlılığa istikamet kazandırır. Böylece emrin merkezinde yalnız dış davranış değil, kime ait olunduğu ve yönelişin kimin için arıtıldığı vardır.

Bu iç yönelim bedensel, ritüel ve ekonomik biçim kazanır. `ق و م B005` namazı kurmak ve sürdürmek, `ص ل و B003` farz ibadet, `ء ت ي B002` zekâtı vermek, `ز ك و B001/B002/B003` ise büyüme, arınma ve malî hakkı yerine getirmek olarak etkinleşir. Namaz dikey bağlılığı süreklileştirirken zekât aynı tevhidî sadakati mülkiyet alanında sınar: Allah’a has kılınan din, malın da mutlak ve bölünmez bir benlik uzantısı sayılmasına izin vermez. Bu bütün, `د ي ن B001` ve `ق و م B008` ile “dosdoğru din” adını alır.

`د ي ن` kökü ibadet düzenini sonuç ve hesapla birleştirir. Din, yalnız inanç etiketi değil; itaat (`د ي ن B001`), yerleşik yol (`B005`), vicdanî güven (`B007`), hesap ve karşılık (`B002`) alanıdır. Böylece 6. ayetteki hüküm, önceki ayetten kopuk bir tehdit değildir: 5. ayette sunulan emir, ibadet, arınma ve paylaşım düzenine verilen cevabın sonucudur.

6. ayet ters mekanizmayı kurar. `ك ف ر B003/B006` hakikati örtme ve reddetmeyi, `ء ه ل B001` Kitap ehli kimliğini, `ك ت ب B002` yazılı vahiy aidiyetini, `ش ر ك B002` ise Allah’a ortak koşmayı taşır. Metin, topluluk adlarını tek başına kurtuluş garantisi yapmaz; aidiyet, ilahî emre verilen cevapla sınanır. İhlasın ortaklığı dışarıda bıraktığı yerde şirk bağlılığı böler; hakikat açığa çıkmışken küfür onu örter.

Bu ters yöneliş `ن و ر B002` ile cehennem ateşine, `خ ل د B001/B002` ile orada kalıcılığa, `ش ر ر B001` ile ahlaki kötülük hükmüne ulaşır. “Yaratılmışların en kötüsü” ifadesindeki `ب ر ء root_000099:B001` ve `ب ر ء root_000100:B001`, mahkûm edilenleri yaratılmışlık ve sorumluluk alanının dışına çıkarmaz. Birincil mekanizma bu nedenle şöyledir: **emir tevhidî bağlılık kurar; ihlas bölünmeyi temizler; haniflik yön verir; namaz bu yönü ayakta tutar; zekât onu maddi paylaşımda gerçekleştirir; bunların bütünü dosdoğru din olur. Hakikati örtmek ve ortak koşmak bu yapıyı tersine çevirerek kalıcı cezaya ve yaratılmışlar içinde ahlaki bir hükme götürür.**

## Etkinleştirilmiş dal tablosu

| Kök | Etkin dallar |
|---|---|
| `ء م ر` | `B001 [B]` emredilen dinî iş ve durum; `B002 [A]` ibadet, namaz ve zekâta yönelten ilahî emir; `B003 [B]` emrin arkasındaki yetki; `B004 [C/B]` itaate bağlı büyüme ve bereket; `B005 [C]` namaz için ritüel işaret ve tayinli zaman; `B006 [C/B]` küfür ve cehennemde somutlaşan ağır iş; `B007 [C]` bağlayıcı emrin karşısındaki müzakere zemini; `B008 [C]` düşüncesiz takip yoluyla sapma; `B009 [C]` genç hayvan ve ritüel tedarik altlığı; `B010 [C/B]` Allah, yaratma ve yargılanan varlıklar arasında ilahî var ediş; `B011 [C]` ceza alanındaki uzak silah ucu imgesi. |
| `ع ب د` | `B001 [B]` Allah’a hizmetin altındaki mülkiyet/kulluk statüsü; `B002 [A]` Allah’a has kulluk; `B003 [A]` ibadet ve itaat; `B004 [C/B]` gönüllü ihlasın karşıtı zorlayıcı köleleştirme; `B005 [C]` teslimiyetin bedensel boyun eğme imgesi; `B006 [B]` ibadetle Allah’ı yüceltme; `B007 [C]` dosdoğru dindeki güç ve sağlamlık; `B008 [C/B]` ibadeti reddeden kibir ve öfke; `B009 [C]` düzenli ritüel harekette acele ve kısa gecikme; `B010 [C]` bölünmüş cemaatlerde farklı yönlere dağılma; `B011 [C]` mahkûmların çözülmesi ve yolda kalması; `B012 [C]` kuyrukta korunan koku havanı/ritüel kap altlığı. |
| `ء ل ه` | `B001 [A]` ibadet ve ibadet edilen; `B002 [A]` Allah özel adı, besmelede de etkin. |
| `خ ل ص` | `B001 [A]` karışımdan arınmış ihlas; `B002 [C]` bağdan kurtulma ve cehennemden selamet; `B003 [C]` yönelişin ilahî hedefine ulaşması; `B004 [A]` ortaklıktan kesin ayrılma; `B005 [A]` dini ve niyeti Allah’a has kılma; `B006 [B]` saf bağlılıkla seçkinleşme; `B007 [B]` Allah ve ibadet topluluğuyla arı yakınlık; `B008 [C]` maddi berraklaştırmadan manevi arınmaya imge. |
| `د ي ن` | `B001 [A]` itaat ve teslimiyet olarak din; `B002 [B]` hesap ve karşılık; `B003 [C/B]` zekâtla etkinleşen malî yükümlülük; `B004 [C/B]` emir-ceza yapısında boyunduruk ve sahiplik; `B005 [B]` yerleşik yol ve alışılmış hâl; `B006 [C]` otorite ve hukuk altında düzenlenmiş dinî toplum; `B007 [B]` ihlasın gerektirdiği vicdanî güven ve tanıklık. |
| `ح ن ف` | `B001 [C]` yönelmenin somut altlığı olarak bedensel eğrilik; `B002 [B]` doğru dine yönelme hareketi; `B003 [A]` yüzeyde hanif yöneliş; `B004 [B]` namaz ve zekâtla beliren İbrahimî ritüel işaretler; `B005 [C]` karşılaştırılan topluluklarda dinî soy ve kimlik. |
| `ق و م` | `B001 [C/B]` Kitap ehli ve müşrikler olarak insan grupları; `B002 [B]` namazda bedensel kıyam; `B003 [B]` emredilen fiillere kalkışma azmi; `B004 [B]` dini ve namazı koruyup sürdürme; `B005 [A]` namazı kurma ve yerine getirme; `B006 [C/B]` cehennemde makam ve devamlı kalış; `B007 [C]` emir ve yükümlülükte başkasının yerini tutma; `B008 [A]` dosdoğru dinin doğruluğu; `B009 [B]` zekâtın desteklediği geçim; `B010 [C/B]` zekât borcunda değer biçme; `B011 [C]` kıyam ve ritüel duruştaki beden yapısı; `B012 [C]` maddi dik durma aygıtı; `B013 [B]` ebedî cezanın gerektirdiği diriliş ve yargı; `B014 [C/B]` ilahî emirle küfür arasındaki karşı koyuş; `B015 [C/B]` zekât ve hükümde eşit ölçü/değer; `B016 [C]` cezada durma ve tükenme; `B017 [C]` namaz vakti altlığı olarak öğle kıyamı; `B018 [C]` mal, yükümlülük ve zekâtla bağlantılı pazar; `B019 [C/B]` ateşle etkinleşen bedensel ağrı; `B020 [C]` geniş sadaka/hayvan rezervuarındaki hayvan hastalığı; `B021 [C]` dosdoğru dini görememenin körlük imgesi. |
| `ص ل و` | `B001 [B]` ateş ve sıcaklığıyla karşılaşma; `B002 [B]` dua, övgü ve rahmet; `B003 [A]` farz namaz; `B004 [C]` şirk ve yakalanma alanındaki tuzak; `B005 [C]` ritüel duruştaki kalça/yan altlığı; `B006 [C/B]` dinî bağlılık ve düzenli ibadette önderi izleme; `B007 [B]` namaz ve ibadet mekânları; `B008 [C]` kuyrukta korunan dövme taşı/ev içi hazırlık; `B009 [C]` büyüme ve sadaka kaynaklarına bağlı bitki/otlak. |
| `ء ت ي` | `B001 [C/B]` verme fiilinin altındaki gelme/getirme hareketi; `B002 [A]` zekâtı verme; `B003 [B]` dinî emre doğru araçla yaklaşma; `B004 [C]` rızık ve arınma altlığı olarak açılmış su yolu; `B005 [C]` kuvvetli geliş imgesi olarak sel; `B006 [C/B]` adlandırılmış topluluklarda dışarıdan gelen ve sınır; `B007 [B]` zekâtın ürettiği verim ve artış; `B008 [B]` zorunlu ödeme/harç; `B009 [C]` verme ve hareket alanındaki hayvan yürüyüşü; `B010 [C]` doğru yol için yol ve yüzünü çevirme imgesi; `B011 [B]` cehennem sonucunda helake yetişilme; `B012 [C]` büyüme ve yaratılmış hayat köprülerindeki üreme/hayvan dalı; `B013 [C]` emredilen fiilleri yerine getiren etkili fail olma. |
| `ز ك و` | `B001 [A]` zekâttaki büyüme ve artış; `B002 [A]` ihlaslı dosdoğru dine bağlı arınma; `B003 [A]` zekât ve malî hak; `B004 [B]` emredilen uygulamanın elverişliliği; `B005 [C]` ölçülmüş malî yükümlülükte çift/eş ölçü. |
| `ك ف ر` | `B001 [B]` küfrün altındaki örtme imgesi; `B002 [C/B]` inkâr ve cehennemle ilişkili karanlık örtü; `B003 [A]` hakikati reddetme ve örtme; `B004 [B]` nimeti nankörlükle örtme; `B005 [B]` dinî yükümlülükten uzaklaşma; `B006 [A]` inkârcı topluluğun yüzey adı; `B007 [C/B]` ilahî emre karşı itaatsizliğe sürüklenme; `B008 [C]` zekât büyümesine bağlı tohumu örtme; `B009 [C/B]` günahı örtme/silme ve cezadan arınma karşıtlığı; `B010 [C]` meyve örtüsü ve hasat; `B011 [C]` uzak maddi/ritüel kâfur dalı; `B012 [C]` cehennem için uzak kopuk yer imgesi; `B013 [C]` gizleme ve sapmış yol imgesi olarak saklı geçit; `B014 [B]` ibadeti reddetmenin karşıtı eğilmiş teslimiyet; `B015 [C]` “yaratılmışların en kötüsü” sıralamasının taç/statü örtüsü. |
| `ء ه ل` | `B001 [A]` Kitap ehli olarak dinî aidiyet; `B002 [C]` evlilik yoluyla hane; `B003 [B]` dosdoğru dine cevapla sınanan ehliyet; `B004 [C]` yerleşik toplum ve mahkûm ikametgâhı; `B005 [C]` ateş sonucunun karşıtı karşılama ve kolaylık; `B006 [C]` ateş bağlamında erimiş yağ/pişirme imgesi. |
| `ك ت ب` | `B001 [C/B]` yazı ve topluluk yapısında unsurları birleştirme; `B002 [A]` Kitap ehlini tanımlayan yazılı Kitap; `B003 [B]` emir ve cezanın arkasındaki bağlayıcı hüküm; `B004 [B]` adlandırılmış dinî gruba/kütüğe yazılma; `B005 [C/B]` kulluk, borç ve özgür bırakmayı bağlayan mükâtebe sözleşmesi. |
| `ش ر ك` | `B001 [B]` şirkin ve kaynak tahsisi köprüsünün altındaki ortaklık; `B002 [A]` Allah’a ortak koşma; `B003 [C]` evlilik/akrabalık ortaklığı; `B004 [C]` bağ imgesi olarak ayakkabı kayışı; `B005 [C]` doğru yolun karşıtı yol izleri; `B006 [C]` yakalanma ve tehlike altlığı olarak avcı tuzağı; `B007 [C]` tekrarlanan ritüel fiillerde hızlı ardışıklık; `B008 [C/B]` bölünmemiş ihlasın karşıtı bölünmüş/meşgul zihin. |
| `ن و ر` | `B001 [B]` ateşten çıkan aydınlık ve dinî körlüğün karşıtı; `B002 [A]` cehennemin yanan ateşi; `B003 [C/B]` ateşi uzaktan görme ve yaklaşan ceza; `B004 [C]` zekât artışına bağlı ağaç çiçeği; `B005 [C]` dinî hidayet için işaret/fener; `B006 [C]` ibadeti reddetmede kaçış; `B007 [C/B]` gruplar arasında ve ateş hükmünde alevlenen düşmanlık; `B008 [C]` ateş ve beden alanındaki duman pigmenti; `B009 [C]` arınma/beden altlığında sürülen kireç; `B010 [C/B]` küfürle bağlantılı şaşırtma; `B011 [C/B]` hakikati örtmenin karşıtı açıklık ve görünürlük. |
| `خ ل د` | `B001 [A]` cehennemde kalıcılık; `B002 [B]` ceza yerinde tutunup kalma; `B003 [C]` maddi kalıcılık imgesi olarak sabit beden süsü; `B004 [C/B]` ihlas veya küfürde yerleşmiş kanaat; `B005 [S]` pasajla görünür bağı olmayan kör kemirgen uzmanlaşması. |
| `ش ر ر` | `B001 [A]` yaratılmışların en kötüsündeki kötülük; `B002 [C]` kuyrukta korunan güneşte kurutma/yemek hazırlama; `B003 [B]` cehennem ateşiyle etkinleşen uçuşan kıvılcım; `B004 [C]` cezada parçalama ve silkme; `B005 [C]` ateş bağlamında kızartma ve damlayan yağ; `B006 [C]` kötülük ve cezanın sürüklenen yükleri; `B007 [C/B]` kişinin kendini bütünüyle ibadete veya yıkıcı kötülüğe atması; `B008 [C/B]` kötülüğü dışa vurup hükmü görünür kılma; `B009 [C]` somut zarar imgesi olarak küçük zararlı canlı; `B010 [C]` gençlik gücü ve istek; `B011 [C/B]` reddeden gruplar arasındaki kavga; `B012 [C]` büyüme/zekât kümesindeki bitki dalı. |
| `ب ر ء` | `root_000099:B001 [A]` yaratılmışların en kötüsündeki yaratma; `root_000099:B002 [C/B]` arınma, ret ve hükümle etkinleşen ahlaki ibra/ayrılma; `root_000099:B003 [C]` cehennem acısının karşıtı iyileşme; `root_000099:B004 [C/B]` dinî borç ve zekâtla ilişkili alacaktan kurtulma; `root_000099:B005 [C]` namaz, arınma ve ihlasa bağlı bedensel/ritüel temizlik; `root_000099:B006 [C]` ritüel zaman altlığında özel gece/gün adı; `root_000099:B007 [C]` gizleme ve tuzak alanında avcı siperi; `root_000100:B001 [A]` yaratmaya doğrudan etkin ikinci kaynak dalı; `root_000100:B002 [C/B]` sorumluluktan ibra ve ahlaki ayrılma; `root_000100:B003 [C]` ateş/ağrı karşısında iyileşme; `root_000100:B004 [C/B]` zekât ve bağlayıcı hükümle mali sorumluluktan kurtulma; `root_000100:B005 [C]` arınma/namaz alanında üreme ve ritüel temizlik; `root_000100:B006 [C]` ritüel zaman altlığında gece/gün adı; `root_000100:B007 [C]` tuzak ve örtme alanında gizli avcı sığınağı. |

## İkincil aktivasyon tablosu

Bu yükseltmeler birincil anlamları değiştirmez; birincil mekanizmanın hukukî, ekonomik, toplumsal, tarımsal ve bedensel altlıklarını görünür kılar.

| Kök/dal | İlk | İkincil | Kazandırdığı okuma |
|---|---:|---:|---|
| `ء م ر B004` | `C/B` | `B` | Zekât emri, itaati bereket ve büyüme üreten bir emir olarak güçlendirir. |
| `ع ب د B004` | `C/B` | `B` | Gönüllü ihlas ile zorlayıcı boyunduruk arasındaki farkı keskinleştirir. |
| `د ي ن B004` | `C/B` | `B` | İtaat olarak dinin arkasında sahiplik, boyun eğdirme ve hüküm karşıtlığını tutar. |
| `د ي ن B003` | `C/B` | `B` | Zekâtı, değer biçilen ve hesabı görülen malî yükümlülük alanına bağlar. |
| `ب ر ء root_000099:B004` | `C/B` | `B` | Borç, ortak mülk ve sözleşme üzerinden alacaktan/sorumluluktan kurtulma portu açar. |
| `ب ر ء root_000100:B004` | `C/B` | `B` | Aynı malî ibra mekanizmasını ikinci kaynak kimliğini silmeden destekler. |
| `ك ت ب B005` | `C/B` | `B` | Kulluk, yazılı yükümlülük, borç ve özgür bırakmayı mükâtebe sözleşmesinde üçgenler. |
| `ق و م B010` | `C/B` | `B` | Zekâtın ölçülen değerini ve hükümdeki hesabı muhasebe altlığına bağlar. |
| `ك ف ر B009` | `C/B` | `B` | Hakikati örtmenin karşısına günahı silme/örtme işlemini koyar. |
| `ب ر ء root_000099:B002` | `C/B` | `B` | Arınma ve günahın silinmesinden ahlaki ibraya geçiş kurar. |
| `ب ر ء root_000100:B002` | `C/B` | `B` | Sorumluluk, arınma ve ayrılma kanıtlarını ikinci kaynak portunda korur. |
| `ك ف ر B008` | `C` | `C/B` | Tohumu örtmeyi, zekâtın verim ve büyüme üretmesine tarımsal karşı-imge yapar. |
| `ك ف ر B010` | `C` | `C/B` | Meyve örtüsü, verme ve hasadı üretken örtme kümesinde birleştirir. |
| `ن و ر B004` | `C` | `C/B` | Ateş kök alanında olumlu ağaç çiçeği, zekât büyümesinin hayat imgesini açar. |
| `ء ت ي B006` | `C/B` | `B` | Topluluk aidiyetini dışarıdan gelen/sınır portuyla sınanan kimlik hâline getirir. |
| `ق و م B001` | `C/B` | `B` | Kitap ehli ve müşrikleri adlandırılmış insan grupları olarak belirginleştirir. |
| `ء ت ي B010` | `C` | `C/B` | Hanif yöneliş için yol ve doğru yüzlenme geometrisi sağlar. |
| `ش ر ك B005` | `C` | `C/B` | Şirki, doğru yolun karşısındaki bölünmüş yol izleri olarak somutlaştırır. |
| `ك ف ر B013` | `C` | `C/B` | Örtülmüş hakikati sapmış ve gizli geçit imgesiyle birleştirir. |
| `ح ن ف B001` | `C` | `C/B` | Manevî yönelişin altına eğrilik, duruş ve ağrıdan oluşan bedensel bir imge yerleştirir. |
| `ب ر ء root_000100:B003` | `C` | `C/B` | Dosdoğru yönelişi iyileşme ve onarım analojisine açar. |
| `د ي ن B006` | `C` | `C/B` | Emri yalnız bireysel değil, hukuk ve topluluk düzeni kuran bir yapı olarak okur. |

## İkincil mekanizmalar

1. **Yükümlülük–değerleme–ibra (`B`):** Emir hesap verilebilir bir yükümlülük yaratır; zekât ölçülmüş maddi cevaptır; yazı ve sözleşme sorumluluğu kaydeder; hüküm, borcun sürüp sürmediğini veya ibrayı belirler. Kanıt: `د ي ن B003`, `ق و م B010`, `ك ت ب B005`, `ب ر ء root_000099:B004`, `ب ر ء root_000100:B004`.
2. **Gönüllü ibadete karşı zorlayıcı sahiplik (`B`):** Yaratılmışlık düzeyindeki boyun eğme, ihlasla gönüllü kulluğa dönüşür; reddeden için zorlayıcı hüküm karşıt kutup olarak kalır. Kanıt: `ع ب د B003/B004`, `د ي ن B001/B004`, `ء ل ه B001`.
3. **Topluluk sınırı ve kayıt (`B`):** Dinî ad, miras alınmış bir güvence değil; ihlas, namaz ve zekâtla anlam kazanan bir aidiyet kaydıdır. Kanıt: `خ ل ص B004`, `ك ت ب B004`, `ء ت ي B006`, `ق و م B001`, `ء ه ل B001`.
4. **Üretken örtmeye karşı engelleyici örtme (`C/B`):** Tohum veya meyveyi örten katman büyümeyi hazırlarken yüzeydeki küfür hakikati örter; benzer maddi işlem zıt ahlaki sonuçlara gider. Kanıt: `ء ت ي B007`, `ز ك و B001`, `ك ف ر B008/B010`, `ن و ر B004`.
5. **Arınma–günahın silinmesi–ibra döngüsü (`B`):** İhlas ve zekât arındırır; arınmış davranış günahı örter/siler; bu da ahlaki sorumluluktan ibra ihtimalini açar. Kanıt: `ز ك و B002`, `ك ف ر B009`, `ب ر ء root_000099:B002`, `ب ر ء root_000100:B002`.
6. **Doğru güzergâha karşı bölünmüş izler (`C/B`):** Haniflik ve dosdoğru din, doğru yüzlenme/yol; şirk ve küfür ise çatallanmış iz ve gizli geçit geometrisi kazanır. Kanıt: `ء ت ي B010`, `ش ر ك B005`, `ك ف ر B013`.
7. **İyileşme olarak bedensel doğrulma (`C/B`):** Eğrilik, namaz duruşu, ağrı ve iyileşme; dosdoğru dinin bozulmuş hâli yeniden yöneltmesi için ihtiyatlı bir beden analojisi kurar. Kanıt: `ح ن ف B001`, `ق و م B019`, `ص ل و B005`, `ب ر ء root_000100:B003`.

## Grafik-hazır kök ve kenar açıklaması

### Düğümler

`ء م ر`, `ع ب د`, `ء ل ه`, `خ ل ص`, `د ي ن`, `ح ن ف`, `ق و م`, `ص ل و`, `ء ت ي`, `ز ك و`, `ك ف ر`, `ء ه ل`, `ك ت ب`, `ش ر ك`, `ن و ر`, `خ ل د`, `ش ر ر`, `ب ر ء`

`ب ر ء` tek kök düğümüdür; `root_000099:*` ve `root_000100:*` kimlikleri yalnız kenar portlarında kaynak kanıtı olarak korunur.

### Birincil ve güçlü etkin kenarlar

| Kaynak | Hedef | Portlar | İlişki |
|---|---|---|---|
| `ء م ر` | `ع ب د` | `ء م ر B002/B003 → ع ب د B002/B003` | ilahî emir → kulluk ve ibadet |
| `ع ب د` | `ء ل ه` | `ع ب د B002/B003 → ء ل ه B001/B002` | ibadet → yalnız Allah |
| `ع ب د` | `خ ل ص` | `ع ب د B003/B004 → خ ل ص B001/B004/B005` | gönüllü kulluk → arınmış bağlılık |
| `خ ل ص` | `د ي ن` | `خ ل ص B001/B005 → د ي ن B001/B005/B007` | ihlas → Allah’a has din |
| `خ ل ص` | `ش ر ك` | `خ ل ص B004 → ش ر ك B001/B002` | özel kılma → ortaklığın dışlanması |
| `د ي ن` | `ح ن ف` | `د ي ن B001/B005 → ح ن ف B002/B003` | itaat yolu → doğru yönelim |
| `ح ن ف` | `ق و م` | `ح ن ف B002/B003 → ق و م B003/B005/B008` | yönelme → doğrulma ve sürdürme |
| `ق و م` | `ص ل و` | `ق و م B002/B005 → ص ل و B002/B003/B007` | kıyam/ikame → namaz |
| `ء ت ي` | `ز ك و` | `ء ت ي B002/B007/B008 → ز ك و B001/B002/B003` | verme → zekât, arınma ve artış |
| `ز ك و` | `د ي ن` | `ز ك و B002/B003/B004 → د ي ن B001/B003` | arınma ve malî hak → dinî yükümlülük |
| `ء م ر` | `ك ت ب` | `ء م ر B002 → ك ت ب B003` | emir → bağlayıcı hüküm |
| `ك ف ر` | `ش ر ك` | `ك ف ر B003/B006 → ش ر ك B002` | hakikati örtme → ortak koşma |
| `ك ف ر` | `ن و ر` | `ك ف ر B002/B003 → ن و ر B002/B003` | inkâr → ateş ve görünür uyarı |
| `ن و ر` | `خ ل د` | `ن و ر B002/B007 → خ ل د B001/B002/B004` | ateş → kalıcı ceza hâli |
| `خ ل د` | `ش ر ر` | `خ ل د B001/B004 → ش ر ر B001/B008` | yerleşmiş reddediş → görünür kötülük hükmü |
| `ش ر ر` | `ب ر ء` | `ش ر ر B001 → ب ر ء root_000099:B001/root_000100:B001` | “en kötü” → yaratılmışlar içinde ahlaki sınıflandırma |

### İkincil/keşif kenarları

| Kaynak | Hedef | Portlar | İlişki |
|---|---|---|---|
| `د ي ن` | `ب ر ء` | `د ي ن B003 → ب ر ء root_000099:B004/root_000100:B004` | yükümlülük → ibra veya süren sorumluluk |
| `د ي ن` | `ق و م` | `د ي ن B003 → ق و م B010/B015` | borç → değerleme ve ölçülmüş hak |
| `خ ل ص` | `ك ت ب` | `خ ل ص B004 → ك ت ب B004` | özel aidiyet → topluluk kaydı |
| `ز ك و` | `ك ف ر` | `ز ك و B002 → ك ف ر B009` | arınma → günahın silinmesi |
| `ك ف ر` | `ب ر ء` | `ك ف ر B009 → ب ر ء root_000099:B002/root_000100:B002` | günahı örtme → ahlaki ibra |
| `ص ل و` | `ن و ر` | `ص ل و B003/B001 → ن و ر B002` | kurulmuş ibadet ilişkisi ↔ dayatılan ateş karşılaşması |
| `ء م ر` | `ز ك و` | `ء م ر B004 → ز ك و B001` | emir → bereket ve büyüme |
| `خ ل ص` | `ء ت ي` | `خ ل ص B004 → ء ت ي B006` | özel kılma → topluluk sınırı |
| `ء ت ي` | `ك ف ر` | `ء ت ي B007 → ك ف ر B008/B010` | verim → tohum/meyve örtüsü |
| `ك ف ر` | `ن و ر` | `ك ف ر B008/B010 → ن و ر B004` | üretken örtü → çiçeklenme |
| `ء ت ي` | `ش ر ك` | `ء ت ي B010 → ش ر ك B005` | doğru yol → bölünmüş izler karşıtlığı |
| `ح ن ف` | `ب ر ء` | `ح ن ف B001 → ب ر ء root_000100:B003` | eğrilik → iyileşme/doğrulma analojisi |

## Most surprising discoveries

1. **Dosdoğru dinin bir yükümlülük ve ibra ekonomisi vardır.** `د ي ن B003`, `ق و م B010`, `ك ت ب B005` ve iki `ب ر ء ...:B004` portu; emri yükümlülük, zekâtı ölçülmüş cevap, hükmü de sorumluluğun sürmesi veya kalkması olarak gösterir. Bu, “din”i borca indirgemez; namaz, zekât ve yargının neden aynı mekanizmada bulunduğunu açıklar.
2. **İhlas aynı zamanda bir sahiplik sınırıdır.** `خ ل ص B004 ↔ ش ر ك B001 ↔ ك ت ب B004` hattında bağlılık ve mülkiyet doğru özneye tahsis edilir. Şirk ilahî bağlılığı böler; zekât yükümlülüğünü çarpıtmak ise maddi bağlılığı böler. Tevhid, yalnız sözde değil, tahsis ve paylaşımda sınanır.
3. **Vermek eksiltmek yerine üretir.** `ء م ر B004 ↔ ز ك و B001` ve `ء ت ي B007 ↔ ك ف ر B008/B010 ↔ ن و ر B004`, zekâtı ekim imgesiyle düşündürür: eldeki şey çıkar, fakat büyüme ve çiçeklenme üretir. Hakikati örten küfürle tohumu örten ekim aynı maddi imgeyi zıt sonuçlara taşır.
4. **Örtme işlemi ahlaken çift yönlüdür.** `ك ف ر B003` hakikati örter ve sorumluluğu korur; `ك ف ر B009` günahı silme yönünde `ز ك و B002` ve `ب ر ء ...:B002` ile birleşerek ibraya açılır. Belirleyici olan örtme eylemi değil, neyin örtüldüğüdür.
5. **Namaz ile ateş aynı kök rezervuarının karşıt portlarında durur.** `ص ل و B003` emre gönüllü ibadet ilişkisini kurarken `ص ل و B001` ve `ن و ر B002` hüküm ateşiyle dayatılmış karşılaşmayı taşır. Aynı alan, kurulmuş yakınlık ile kaçınılmaz cezai temas arasındaki geçişi hissedilir kılar.
6. **“Yaratılmışların en kötüsü” ifadesinin altında ibra ihtimali hâlâ görünürdür.** Yüzeyde `ب ر ء ...:B001` yaratılmışlığı bildirir; ikincil `...:B002/B004` portları ayrılma, sorumluluk ve ibra yollarını korur. Son hüküm yalnız bir hakaret değil, arınma ve sorumluluktan kurtulma yolu sunulmuşken örtme ve ortaklıkta kalmanın sonucudur.

## Kuyrukta korunan yerel olarak zayıf okumalar

Eritilmiş yağ/pişirme (`ء ه ل B006 ↔ ش ر ر B005`), koku kabı (`ع ب د B012 ↔ ك ف ر B010`), yarış/hız hareketi (`ع ب د B009 ↔ ص ل و B006`), genç hayvan/gençlik (`ء م ر B009 ↔ ش ر ر B010`), ev içi dövme ve yemek hazırlama (`ص ل و B008 ↔ ش ر ر B002`) gibi kümeler mekanik olarak görünürdür. Ateş, ibadet veya zekât bağlamıyla uzaktan ilişki kursalar da pasaj bunların maddi ayrıntılarını söylemez. Bu nedenle rezervuarda `C` veya mevcut `C/B` etiketleriyle tutulmalı, ana mekanizmaya taşınmamalıdır.

## Açık sorular

1. `د ي ن B003` ile kurulan malî yükümlülük okuması, zekâtın pasaj içindeki açık varlığı sayesinde ne ölçüde `B` düzeyinde tutulmalı; nerede yalnız analoji olarak sınırlandırılmalıdır?
2. `ع ب د B004` ve `د ي ن B004` zorlayıcı boyunduruk katmanları, gönüllü ihlası açıklayan karşıt zemin midir, yoksa ceza tarafında bağımsız mekanizma mı kurar?
3. `خ ل ص B004 ↔ ش ر ك B001` sahiplik/tahsis ağı, zekât ile tevhid arasındaki ilişkiyi açıklarken ekonomik dili ne ölçüde genişletebilir?
4. `ك ف ر B008/B010` üretken örtme dalları, yüzeydeki `ك ف ر B003` ile yararlı bir karşı-imge midir, yoksa kök içi çağrışım aşırı anlam yükleme riski taşır mı?
5. `ص ل و B001` ateşle temas portu, namaz–cehennem karşıtlığını gerçekten güçlendiriyor mu; yoksa yalnız biçimsel kök rezervuarı olarak mı kalmalı?
6. `ب ر ء root_000099:*` ve `root_000100:*` kaynakları, aynı düğümde anlamlı paralellik mi sağlıyor, yoksa bazı ikincil dallar için kaynaklar ayrı ağırlıklandırılmalı mı?
7. “Kitap ehli” ve “müşrikler” sınıflandırmasında `ء ت ي B006`, `ق و م B001` ve `د ي ن B006`, miras alınmış kimlik ile fiilî sorumluluk arasındaki sınırı ne kadar güçlü biçimde taşır?
8. `ح ن ف B001 → ب ر ء root_000100:B003` bedensel doğrulma/iyileşme analojisi yorumlayıcı değer taşıyor mu, yoksa yalnız düşük güvenli keşif olarak mı kalmalıdır?
9. Besmelenin rahmet çerçevesi, ateş ve kalıcılık hükmünü arınma/ibra ihtimaliyle birlikte okumaya ne ölçüde izin verir?
10. Pasaj 7–8. ayetlerle birlikte ele alındığında “en kötü yaratılmışlar” karşısındaki “en hayırlı yaratılmışlar” simetrisi bu iki ayetlik mekanizmanın hangi ikincil dallarını yükseltir veya sınırlar?

## Sonuç

S98:5–6, inancı ritüelden ve ekonomiden ayırmaz. Allah’a has kılınan din, doğru yönelişle biçimlenir; namazla ayakta tutulur; zekâtla maddi düzende doğrulanır. Küfür ve şirk ise bu bütünlüğü tersine çeviren örtme ve bölme işlemleridir. İkincil okumalar birincil omurgayı dağıtmadan üç önemli boyut ekler: din hesap verilebilir bir yükümlülük düzenidir; ihlas bağlılık ve mülkiyetin doğru tahsisidir; arınma, günahın silinmesi ve ibra birbirine bağlı süreçlerdir. Tarımsal, bedensel ve sözleşmesel imgeler keşif rezervuarında korunmuş, fakat yalnız mekanizma ve yerel bağ tarafından desteklendikleri ölçüde yükseltilmiştir.
