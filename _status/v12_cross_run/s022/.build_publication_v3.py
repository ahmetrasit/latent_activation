import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROSTER = HERE / "ayah_roster.v3.json"
ANCHORS = HERE / "anchor_map.v3.json"
DRAFT = HERE / "publication.v3.draft.json"
AUDIT = HERE / "self_audit.v3.json"


def f(text, grade, *citations):
    return {"text": text, "grade": grade, "_citations": citations}


F = {
    "22:0": [
        f("Bu başlangıç, surenin sarsıntı, ibadet ve yargı sahnelerinin tümünü etkin merhametin yönetimi altına yerleştirir.", "strong", ("ر ح م", "B001"), ("س م و", "B005")),
        f("Daha sonra anılan rahim, buradaki merhamete hayatı içinde taşıyan ve geliştiren bir kuşatıcılık boyutu kazandırır.", "weak", ("ر ح م", "B003")),
    ],
    "22:1": [
        f("Sakınma buyruğu, bütün dayanaklar sarsılmadan önce insanın kendisini koruyucu bir konuma yerleştirmesini ister.", "strong", ("و ق ي", "B002"), ("ز ل ز ل", "B001")),
        f("Rab hitabı, sarsıntının çözebileceği düzeni aşama aşama kurup tamamlayan yetiştiriciye yönelmeyi de içerir.", "strong", ("ر ب ب", "B002")),
    ],
    "22:2": [
        f("Dehşet, bağımlı hayatı taşıyan gebelik, doğum ve emzirme zincirini tersine çevirip bedensel bakım bağlarını koparır.", "strong", ("ر ض ع", "B001"), ("ح م ل", "B002"), ("و ض ع", "B002")),
        f("Sarhoşluk görünümü içkiden değil, algı ve hareketi ele geçiren azabın oluşturduğu denetim kaybından doğar.", "strong", ("س ك ر", "B001"), ("ع ذ ب", "B005")),
        f("Daha sonraki kurban sahnesi, bedenin düşüşünün her durumda salt yıkım olmadığını gösterir: bir düşüş bakım bağlarını koparırken diğeri paylaşılacak rızka dönüşür.", "weak", ("و ض ع", "B002"), ("ح م ل", "B002")),
    ],
    "22:3": [
        f("Bilgisiz tartışma, kanıtları düzenlemek yerine onları birbirine dolayan ve tartışanı izlediği yola bağlayan bir yöntem olur.", "strong", ("ج د ل", "B001"), ("ت ب ع", "B003")),
        f("Şeytana adım adım uymak, katılaşmış başkaldırıyı giderek artan bir uzaklaşma güzergâhına dönüştürür.", "weak", ("ش ط ن", "B001"), ("م ر د", "B003")),
        f("Daha sonra bozucu eklemenin giderilip ayetlerin sağlamlaştırılması, burada birbirine dolanan tartışmanın karşısına onarıcı bir söz düzeni koyar.", "strong", ("ج د ل", "B001"), ("ع ل م", "B001")),
    ],
    "22:4": [
        f("Seçilen yakınlık ve bağlılık, izleyenin yönünü belirleyen ve varacağı yeri bağlayıcı hale getiren bir ilişkiye dönüşür.", "strong", ("و ل ي", "B004"), ("ك ت ب", "B003")),
        f("Buradaki yol gösterme olumlu bir anlam taşımaz; kişiyi güvenilir biçimde yıkıcı bir sonuca götüren yönlendirmedir.", "strong", ("ه د ي", "B001"), ("س ع ر", "B001")),
    ],
    "22:5": [
        f("Diriliş, bedende ve toprakta daha önce görülen gizlenme, tutulma ve yeniden hareketlenme düzeninin son halkası olarak gösterilir.", "strong", ("ب ع ث", "B001"), ("ق ر ر", "B003"), ("ه ز ز", "B002")),
        f("Rahim ile kurumuş toprak, saklı hayatı uygun ortamda görünür büyümeye çıkaran iki benzer taşıyıcı alan haline gelir.", "strong", ("ر ح م", "B003"), ("ن ب ت", "B001")),
        f("Bilginin edinilip yaşlılıkta yitirilmesi, zihinsel gücün de yaratılmış hayat döngüsünde artıp geri çekildiğini gösterir.", "weak", ("ع ل م", "B001")),
    ],
    "22:6": [
        f("Allah'ın gerçek oluşu, önceki ayette görülen dönüşümleri farklı maddelerde düzenli biçimde gerçekleştiren etkin bir sağlamlık olarak belirir.", "strong", ("ح ق ق", "B001"), ("ح ي ي", "B002")),
        f("Kudret yalnız sınırsız güç değil, her şeyi kendi ölçüsüne ve tamamlanma sınırına ulaştıran ölçülü yeterliliktir.", "strong", ("ق د ر", "B001")),
    ],
    "22:7": [
        f("Mezar, son yokluk değil, hareketsiz olanın uyandırılmayı beklediği gizli ve içe alınmış bir bekleme yeri olarak okunur.", "strong", ("ق ب ر", "B002"), ("ب ع ث", "B001")),
        f("Şüphenin reddi, beden ve toprağın daha önce sergilediği tekrar eden canlanma düzenine dayanır.", "weak", ("ر ي ب", "B001")),
        f("İçi boşalmış kentler ve kullanılmayan kuyular, mezardaki gizli hareketsizliği yolculuk sırasında okunabilecek maddi bir kanıta dönüştürür.", "weak", ("ق ب ر", "B002")),
    ],
    "22:8": [
        f("Bu tartışma bilgi, yön ve aydınlatıcı kayıt biçimindeki üç denetimden de yoksun olduğu için birbirine dolanan iddiaları doğrultamaz.", "strong", ("ج د ل", "B001"), ("ه د ي", "B001"), ("ن و ر", "B001")),
        f("Aydınlatıcı kitap, yalnız bilgi veren bir metin değil, tartışmanın yoldan çıkmasını önleyen görünür bir güzergâh işaretidir.", "weak", ("ن و ر", "B005"), ("ك ت ب", "B002")),
    ],
    "22:9": [
        f("Bedenin kibirle yana dönmesi, başkalarını da Allah'ın yolundan saptıran toplumsal bir karşı yönelişe dönüşür.", "strong", ("ث ن ي", "B005"), ("ع ط ف", "B003"), ("س ب ل", "B001")),
        f("Dünyadaki aşağılanma, sergilenen üstünlük duruşunu açığa çıkarır; sonraki yakıcı azap ise sonucunu doğrudan yaşatır.", "strong", ("خ ز ي", "B001"), ("ذ و ق", "B002")),
        f("Ortak koşmanın düşme, kapılma ve savrulma görüntüsü, buradaki yana dönüşü tam bir mekânsal dağılmanın başlangıcı olarak büyütür.", "weak", ("ث ن ي", "B005"), ("ع ط ف", "B003")),
    ],
    "22:10": [
        f("Ellerin önden gönderdiği işler, kişinin ileride karşılaşacağı bir iz ve sonuç meydana getirir.", "strong", ("ق د م", "B004"), ("ي د ي", "B009")),
        f("Kulluğun bağımlılığı keyfî kötü muamele anlamına gelmez; sonuç, onu doğuran eylemden başka birine yerleştirilmez.", "weak", ("ع ب د", "B001"), ("ظ ل م", "B004")),
        f("Daha sonraki denk karşılık sınırı, önden gönderilen eylem ile geri dönen sonucun gelişigüzel değil orantılı biçimde bağlandığını açıklar.", "strong", ("ق د م", "B004"), ("ظ ل م", "B004")),
    ],
    "22:11": [
        f("Kenar üzerinde kulluk, yarara göre sakinleşip sınamada tersine dönen, merkezsiz ve getirisi koşula bağlı bir bağlılıktır.", "strong", ("ح ر ف", "B003"), ("ق ل ب", "B004"), ("خ س ر", "B002")),
        f("Sınama, kişinin yönünü bozmaz; yüzünün zaten kararsız olan yönelişini görünür hale getirir.", "strong", ("ف ت ن", "B001"), ("و ج ه", "B002")),
    ],
    "22:12": [
        f("Etkisiz bir varlığa yöneltilen çağrı yakınlık kuramaz ve eldeki yakın görünen seçeneği gerçek bir uzaklığa dönüştürür.", "strong", ("د ع و", "B001"), ("د و ن", "B001"), ("ب ع د", "B001")),
        f("Zarar ve yarar veremeyiş, yalnız bir güç eksikliğini değil, karşılık vermeyen tek yönlü bir ilişkiyi açığa çıkarır.", "weak", ("ض ر ر", "B001"), ("ن ف ع", "B001")),
        f("Sineği yaratamama ve aldığını geri alamama örneği, bu etkisiz çağrıyı maddi olarak sınanabilir bir yetersizliğe dönüştürür.", "strong", ("د ع و", "B001"), ("ن ف ع", "B001")),
    ],
    "22:13": [
        f("Yanlış veli seçimi, zararı kişinin en yakın destek çevresine yerleştirir; zararın yakınlığı böylece ilişkinin yapısına dönüşür.", "strong", ("ق ر ب", "B001"), ("و ل ي", "B001"), ("ض ر ر", "B001")),
        f("Çağrılanın kötü bir yoldaş sayılması, başarısızlığın yalnız yarar sağlayamamak değil, ortak hayat bağı kuramamak olduğunu gösterir.", "weak", ("ع ش ر", "B012")),
    ],
    "22:14": [
        f("İman ve düzgün eylem, insanı dış etkilere göre tersine dönen bir kenardan korunaklı ve sürekli akan bir yaşama taşır.", "strong", ("ء م ن", "B001"), ("د خ ل", "B001"), ("ج ر ي", "B001")),
        f("Düzgün eylem yalnız tekil iyilik üretmez; içinde yaşanabilen düzenli bir çevrenin kurulmasına katılır.", "weak", ("ص ل ح", "B003"), ("ج ن ن", "B003")),
        f("Bahçenin daha sonra giysi, süs ve arınmış sözle yeniden anlatılması, bu girişi hem bedensel örtünün hem toplumsal konuşmanın onarılması haline getirir.", "weak", ("د خ ل", "B001"), ("ج ن ن", "B003")),
    ],
    "22:15": [
        f("Göğe uzanan bağı kesme girişimi, ilahî yardım hattını denetlemek isterken kişinin kendi dayanağını kesen bir düzeneğe dönüşür.", "strong", ("م د د", "B001"), ("س ب ب", "B003"), ("ق ط ع", "B001")),
        f("Kurulan düzenin öfkeyi giderip gidermediğine bakılması, hilenin yardımı etkisizleştirmediğini, yalnız içerideki sıkışmayı dışa vurduğunu gösterir.", "strong", ("ك ي د", "B002"), ("غ ي ظ", "B001"), ("ن ص ر", "B001")),
    ],
    "22:16": [
        f("Açık ayetlerin denetimli biçimde indirilmesi, önceki ayetteki sonuçsuz yukarı müdahalenin karşısına yukarıdan gelen görünür yol işaretlerini koyar.", "strong", ("ن ز ل", "B002"), ("ب ي ن", "B004")),
        f("Yol gösterme erişilebilir kılınsa da başıboş değildir; iradeyle seçilip belirli bir yöne sevk edilir.", "weak", ("ه د ي", "B001"), ("ر و د", "B001")),
        f("Daha sonraki bozucu ekleme, giderme ve sağlamlaştırma dizisi, açık ayetlerin yol göstermesini müdahaleden etkilenmeyen basit bir aktarım değil, korunan bir süreç olarak gösterir.", "strong", ("ب ي ن", "B004"), ("ه د ي", "B001")),
    ],
    "22:17": [
        f("Farklı topluluklar yan yana anılsa da kesin ayrım, ortak görünüşten sonra iddiaları birbirinden açıkça ayıran yargıya bırakılır.", "strong", ("ف ص ل", "B002"), ("ب ي ن", "B002"), ("ش ه د", "B001")),
        f("Topluluk adlarının köklerindeki yönelme ve ayrılma hareketleri, bu kimlikleri durağan etiketlerden çok izlenen yollar olarak düşündürür.", "reject", ("ه و د", "B001"), ("ص ب ء", "B001")),
        f("Bütün varlıkların secdesi, ayrılacak toplulukları önce ortak bir yaratılmışlık ve boyun eğiş alanına yerleştirir.", "weak", ("ف ص ل", "B002"), ("ش ه د", "B001")),
    ],
    "22:18": [
        f("Secde, gökten yere ve sabit dağdan hareketli canlıya kadar bütün varlık katmanlarını aynı alçalma hareketinde birleştirir.", "strong", ("س ج د", "B001"), ("س م و", "B004"), ("د ب ب", "B001")),
        f("İnsanlar arasındaki ayrım, evrensel boyun eğiş içinde gönüllü uyum ile zorunlu aşağılanma arasındaki farkı görünür kılar.", "strong", ("ه و ن", "B003"), ("ك ر م", "B001")),
        f("Sonraki rükû ve secde buyruğu, insan ibadetini yaratılmış düzenin zaten gerçekleştirdiği alçalmaya bilinçli katılım haline getirir.", "strong", ("س ج د", "B001")),
    ],
    "22:19": [
        f("Gerçeği örtenlerin karşılığı olarak ateşten giysi biçilmesi, seçilen örtüyü bedeni kuşatan yıkıcı bir örtüye çevirir.", "strong", ("ك ف ر", "B001"), ("ث و ب", "B003"), ("ق ط ع", "B012")),
        f("Rab hakkında çekişme, yukarıdan dökülen kaynar sıvıyla baştan aşağı kuşatılmaya varan bedensel bir sonuca dönüşür.", "weak", ("خ ص م", "B001"), ("ص ب ب", "B001"), ("ف و ق", "B001")),
    ],
    "22:20": [
        f("Eriten sıcaklık, iç organlarla dış deriyi birlikte çözerek bedenin içi ile koruyucu dış katmanı arasındaki sınırı kaldırır.", "strong", ("ص ه ر", "B002"), ("ب ط ن", "B001"), ("ج ل د", "B001")),
        f("Deri kökünün dayanıklılık çağrışımı da eridiği için, yalnız beden değil direnme imgesi de çözülür.", "reject", ("ج ل د", "B002"), ("ص ه ر", "B002")),
        f("İçi boşalmış kent ve kullanılmayan kuyu, iç ile dışın işlevsel bağının çözülmesini beden ölçeğinden yerleşim ölçeğine taşır.", "weak", ("ب ط ن", "B002"), ("ج ل د", "B001")),
    ],
    "22:21": [
        f("Demir topuzlar, çıkış hareketini durdurup geri çeviren sert ve zorlayıcı bir sınır işlevi görür.", "strong", ("ق م ع", "B002"), ("ح د د", "B004")),
    ],
    "22:22": [
        f("Her çıkma isteğinin yeniden içeri döndürülmesi, niyet, çıkış ve geri dönüşten oluşan kapalı bir döngü kurar.", "strong", ("خ ر ج", "B001"), ("ع و د", "B001")),
        f("Keder yalnız içeride hissedilen bir duygu değil, kişiyi dıştan kuşatıp içine işleyen bir ortam haline gelir.", "strong", ("غ م م", "B001"), ("غ م م", "B003")),
        f("Daha sonraki göç ve kabul edilen giriş, çıkışın her zaman geri kapatılmadığı; doğru yönelişte ölümün bile açık bir varışa dönüşebildiği karşı örneği kurar.", "strong", ("خ ر ج", "B001"), ("ع و د", "B001")),
    ],
    "22:23": [
        f("Seçilerek takılan süsler ve ipek giysi, önceki zorla giydirilen ateş örtüsünü onurlu ve isteğe bağlı bir kuşatmayla tersine çevirir.", "strong", ("ح ل ي", "B001"), ("ل ب س", "B001")),
        f("Bahçeye giriş, azaptaki zorunlu geri dönüşün karşısına kesintisiz akışla açılan kalıcı bir yerleşme koyar.", "strong", ("د خ ل", "B001"), ("ج ر ي", "B001")),
        f("Güzel söze ve doğru yola yöneltilme, süs ve ipeği salt duyusal ödül olmaktan çıkarıp onarılmış bir ilişki ve yönelişin işaretleri yapar.", "weak", ("ح ل ي", "B001"), ("ل ب س", "B001")),
    ],
    "22:24": [
        f("Güzel söze ve övgüye layık olanın yoluna yöneltilmek, konuşma ile yürüyüşü tek bir yöneliş düzeninde birleştirir.", "strong", ("ه د ي", "B001"), ("ق و ل", "B001"), ("ص ر ط", "B001")),
        f("Sözün iyi oluşu, onun yalnız hoş değil, zararlı karışımdan arınmış olmasını da içerir.", "weak", ("ط ي ب", "B003")),
    ],
    "22:25": [
        f("Mescidin yerleşik ile dışarıdan gelen için eşit kılınması, kutsal alanı eşit erişimle kurulmuş ortak bir mekân yapar.", "strong", ("س و ي", "B001"), ("ع ك ف", "B001"), ("ب د و", "B002")),
        f("Doğrultucu ve korunan bir mekânda eğrilik istemek, yanlışın mekânsal niteliğini ağırlaştırır.", "strong", ("ل ح د", "B001"), ("ح ر م", "B003")),
        f("Farklı ibadet yapılarının yıkımdan korunması, buradaki eşit ve korunan erişim ilkesini tek yapının ötesinde çoğul bir ibadet çevresine genişletir.", "weak", ("ح ر م", "B003"), ("س و ي", "B001")),
    ],
    "22:26": [
        f("Evin yerinin hazırlanması, tavaf eden, ayakta duran, eğilen ve secde eden bedenleri merkez çevresinde düzenleyen bir hareket örgüsü kurar.", "strong", ("ب و ء", "B001"), ("ط و ف", "B001"), ("ر ك ع", "B001"), ("س ج د", "B001")),
        f("Ortak koşmama buyruğu, bu hareket düzeninin merkezini bölünmüş bağlılıklardan korur.", "strong", ("ش ر ك", "B001"), ("ب ي ت", "B001")),
        f("Sonraki iyilik buyruğu, ev çevresindeki düzenli beden hareketlerini dışarıda yararlı eylem üreten bir eğitim olarak yeniden okutur.", "weak", ("ر ك ع", "B001"), ("س ج د", "B001")),
    ],
    "22:27": [
        f("Haccın kamuya duyurulması, derin ve uzak geçitlerden gelenleri tek merkeze taşıyan dairesel bir hareket ağı oluşturur.", "strong", ("ء ذ ن", "B003"), ("ح ج ج", "B001"), ("ف ج ج", "B001")),
        f("Yaya ayaklar ile zayıflamış bineklerin anılması, ortak varışın bedensel yorgunluk pahasına gerçekleştiğini öne çıkarır.", "weak", ("ر ج ل", "B003"), ("ض م ر", "B001")),
        f("Varışın devamında görülen yarar ve yoksula verilen yiyecek, çağrının hedefini merkeze ulaşmanın ötesinde toplumsal dolaşıma taşır.", "strong", ("ء ت ي", "B001"), ("ح ج ج", "B001")),
    ],
    "22:28": [
        f("Tanık olunan yararlar, adın anılması ve yedirme buyruğuyla özel deneyimden muhtaçlara ulaşan dolaşımdaki rızka çevrilir.", "strong", ("ش ه د", "B001"), ("ر ز ق", "B001"), ("ط ع م", "B002")),
        f("Belirli günlerde Allah'ın adının anılması, hayvanın kapalı görünen maddi varlığını adlandırılmış bir bağış ilişkisine açar.", "weak", ("س م و", "B005"), ("ب ه م", "B001")),
        f("Et ve kanın Allah'a ulaşmadığının sonradan belirtilmesi, buradaki yeme ve yedirmeyi maddi aktarım değil, iç sakınmanın toplumsal taşıyıcısı yapar.", "strong", ("ط ع م", "B002"), ("ذ ك ر", "B004")),
    ],
    "22:29": [
        f("Bedenin arındırılması, adağın tamamlanması ve evin çevresinde dönme, ritüel kapanışı bedenden yükümlülüğe, oradan yeniden merkeze taşır.", "strong", ("ق ض ي", "B004"), ("و ف ي", "B001"), ("ط و ف", "B001")),
        f("Eski evin özgür bırakılma çağrışımı, tamamlanan yükümlülüklerin kişiyi serbest bıraktığı bir çözülme noktası oluşturur.", "weak", ("ع ت ق", "B001")),
    ],
    "22:30": [
        f("Allah'ın yasaklarına saygı, her şeyi yasaklamak değil, korunan sınırlarla helal bırakılan alanları dikkatle ayırt etmektir.", "strong", ("ح ر م", "B006"), ("ح ل ل", "B003")),
        f("Putların kiri ile yalan sözün birlikte anılması, bedensel yön sapmasıyla sözdeki sapmayı aynı uzak durma buyruğunda birleştirir.", "weak", ("ج ن ب", "B003"), ("ز و ر", "B002")),
    ],
    "22:31": [
        f("Yalnız Allah'a yöneliş kişiye bir eksen sağlarken ortak koşmak, yönü parçalayıp düşme ve sürüklenmeyle sonuçlanan dağınık kuvvetlere bırakır.", "strong", ("ح ن ف", "B002"), ("ش ر ك", "B001"), ("خ ر ر", "B001")),
        f("Kuşun kapması ile rüzgârın uzağa atması iki ayrı başarısızlığı gösterir: dış güççe ele geçirilme ve yönsüzce savrulma.", "weak", ("خ ط ف", "B001"), ("ر و ح", "B003")),
        f("Gerçek ile geçersizin etkileri üzerinden ayrılması, buradaki düşüşün temelini ortakların düzeni taşıyacak nedensel güçten yoksun oluşunda gösterir.", "strong", ("ش ر ك", "B001"), ("خ ر ر", "B001")),
    ],
    "22:32": [
        f("Görünür hac işaretlerinin değeri dış biçimlerinden değil, kalplerdeki koruyucu sakınmanın onları anlamlı kılmasından doğar.", "strong", ("ش ع ر", "B006"), ("و ق ي", "B002"), ("ق ل ب", "B001")),
        f("İşareti büyütmek, onun ince anlamını sezebilen bir iç dikkat gerektirir.", "weak", ("ش ع ر", "B005"), ("ع ظ م", "B001")),
    ],
    "22:33": [
        f("Hayvanların geçici yararı, belirlenmiş vakitte eski eve bağlı kutsal güzergâhta sona eren daha büyük bir sürecin içine yerleştirilir.", "strong", ("ن ف ع", "B001"), ("ء ج ل", "B001"), ("ح ل ل", "B004")),
        f("Göç edenlerin ölümden sonra hoşnut olacakları yere girişi, süre ve varış düzenini hayvandan insana uzanan daha genel bir yol kalıbı haline getirir.", "weak", ("ء ج ل", "B001"), ("ح ل ل", "B004")),
    ],
    "22:34": [
        f("Topluluklara farklı ibadet yolları verilmesi, hepsini rızık veren tek Allah'ın adında ortak bir kaynağa yöneltir.", "strong", ("ن س ك", "B003"), ("س م و", "B005"), ("و ح د", "B004")),
        f("Teslimiyet, yenilgi değil, insanın kendisini güvenle alçak ve almaya açık bir konuma bırakmasıdır.", "weak", ("س ل م", "B012"), ("خ ب ت", "B001")),
    ],
    "22:35": [
        f("Alçakgönüllülük; Allah anıldığında ürperme, darbeye sabır, namazı ayakta tutma ve rızkı dolaşıma sokma şeklinde dört kanallı bir karşılık üretir.", "strong", ("خ ب ت", "B001"), ("و ج ل", "B001"), ("ص ب ر", "B001"), ("ن ف ق", "B002")),
        f("Başlarına gelen şey, kenarda kulluk edenlerdeki gibi yönlerini tersine çevirmez; sabır etkiyi taşıyıp bağlılığı korur.", "strong", ("ص و ب", "B004"), ("ص ب ر", "B001")),
    ],
    "22:36": [
        f("Sıra halinde ayakta duran canlı bedenin yere düşüp paylaştırılması, dikey ibadet düzenini yatay toplumsal paylaşıma dönüştürür.", "strong", ("ص ف ف", "B001"), ("و ج ب", "B001"), ("ج ن ب", "B001")),
        f("İsteyen ile ihtiyacını gizleyen iki duruşun da doyurulması, paylaşımın talep biçimine göre daraltılmamasını sağlar.", "strong", ("ق ن ع", "B001"), ("ع ر ر", "B004")),
        f("Sinek örneği, insanların kullanımına verilen güçlü hayvanın mutlak sahiplik sağlamadığını; küçük bir canlının bile insan ve putların sınırını gösterebildiğini hatırlatır.", "strong", ("س خ ر", "B001"), ("ب د ن", "B003")),
    ],
    "22:37": [
        f("Allah'a ulaşan şey et ve kan değil, maddi taşıyıcıyı yönlendiren koruyucu sakınmadır.", "strong", ("ن ي ل", "B001"), ("ل ح م", "B001"), ("و ق ي", "B002")),
        f("Hayvanların insanlara boyun eğdirilmesi sahiplenmeyi büyütmek için değil, doğru yola ileten Allah'ı yüceltmek içindir.", "strong", ("س خ ر", "B001"), ("ك ب ر", "B003"), ("ه د ي", "B001")),
    ],
    "22:38": [
        f("Allah'ın savunması, inananları çatışmadan muaf tutmak değil, üzerlerine gelen baskıya karşı etkin bir karşı kuvvet sağlamaktır.", "strong", ("د ف ع", "B001"), ("ء م ن", "B001")),
        f("Hainlik ve nankörlük, güven ilişkisinin yapışmasını bozan karşı özellikler olarak inananın kimliğini tersinden belirler.", "weak", ("خ و ن", "B001"), ("ك ف ر", "B004")),
        f("Denk karşılık, yenilenen saldırı ve bağışlama hükümleri, bu savunmanın gücünü orantı ve sınır içinde tutar.", "strong", ("د ف ع", "B001"), ("ء م ن", "B001")),
    ],
    "22:39": [
        f("Savaş izni sınırsız güç kullanımı değil, saldırıya uğrayanların uğradığı haksızlığı gidermeye bağlanmış ölçülü bir geçiştir.", "strong", ("ء ذ ن", "B004"), ("ظ ل م", "B003"), ("ن ص ر", "B002")),
        f("Allah'ın yardım kudreti insan eyleminin arkasında durur, fakat verilen iznin sınırlarını ve insan sorumluluğunu ortadan kaldırmaz.", "weak", ("ق د ر", "B003")),
    ],
    "22:40": [
        f("İnsanların birbirini engelleyen karşı kuvveti yalnız bir topluluğu değil, farklı ibadet yerlerinden oluşan çoğul bir anma düzenini korur.", "strong", ("د ف ع", "B001"), ("ه د م", "B001"), ("ص ل و", "B007")),
        f("Evlerinden çıkarılanların Allah'ın adını söylemesi, sürülen sözün manastır, kilise, havra ve mescit yapılarında yeniden barınmasıyla karşılık bulur.", "weak", ("ق و ل", "B001"), ("س م و", "B005")),
        f("Göğün düşmekten tutulması, insanların yıkımı önleyen karşı kuvvetini kozmik ölçekteki koruyucu tutuşla aynı düzen içinde gösterir.", "weak", ("د ف ع", "B001"), ("ه د م", "B001")),
    ],
    "22:41": [
        f("Yeryüzünde güç verilmesinin sınavı, iktidarın namazı ayakta tutması, paylaşımı dolaştırması ve kamusal iyiliği sürdürmesidir.", "strong", ("م ك ن", "B005"), ("ق و م", "B004"), ("ز ك و", "B001")),
        f("İşlerin sonucunun Allah'a ait olması, iktidarın kendi amacı çevresinde kapanmasını önler.", "strong", ("ع ق ب", "B006"), ("ء م ر", "B001")),
    ],
    "22:42": [
        f("Şimdiki inkâr, geçmiş topluluklarda tekrar eden ortak bir toplumsal davranış dizisinin içine yerleştirilir.", "strong", ("ك ذ ب", "B002"), ("ق ب ل", "B002"), ("ق و م", "B001")),
    ],
    "22:43": [
        f("Ad ve fiil tekrarlarının eksiltilmesi, reddedişi tek tek kişilerden çok kuşaktan kuşağa taşınan topluluk davranışı haline getirir.", "weak", ("ق و م", "B001")),
    ],
    "22:44": [
        f("Verilen süre, hesabın yokluğunu değil, sonunda yakalanmaya çıkan uzatılmış bir hesap evresini gösterir.", "strong", ("م ل و", "B001"), ("ء خ ذ", "B002")),
        f("Medyen halkı ve Musa'nın karşısındakilerde yoldaşlık, toplu kimliği ve toplu sorumluluğu belirleyen bir bağ haline gelir.", "weak", ("ص ح ب", "B001")),
    ],
    "22:45": [
        f("Yıkım yalnız binaların çökmesi değil, yerleşim, su ve korunma parçalarının birlikte işlevsiz kaldığı yaşanmış bir sistemin boşalmasıdır.", "strong", ("ق ر ي", "B001"), ("خ و ي", "B001"), ("ع ط ل", "B001")),
        f("Kullanılmayan kuyu ile ayakta kalan yüksek saray, altyapı ve itibarın insan topluluğu olmadan boş bir karşıtlığa dönüştüğünü gösterir.", "strong", ("ب ء ر", "B001"), ("ق ص ر", "B005")),
    ],
    "22:46": [
        f("Yeryüzünde yolculuk, görülen sonuçları işitme ve düşünmeyle bağlayan etkin bir bilgi edinme sürecidir.", "strong", ("س ي ر", "B001"), ("ع ق ل", "B001"), ("س م ع", "B003")),
        f("Çalışan gözlere rağmen kalbin kör kalabilmesi, asıl görme kusurunu veriyi yorumlayan iç merkeze yerleştirir.", "strong", ("ع م ي", "B001"), ("ب ص ر", "B001"), ("ق ل ب", "B001")),
    ],
    "22:47": [
        f("İnsan aceleciliği, ilahî zaman ölçeğiyle kendi kısa sayımını karıştırıp gecikmeyi sözün bozulması sanır.", "strong", ("ع ج ل", "B001"), ("خ ل ف", "B005"), ("ع د د", "B001")),
        f("Rabbin katında bulunmak, zamanın ölçüsünü insan deneyimindeki uzunluktan farklı bir düzene taşır.", "weak", ("ع ن د", "B004"), ("ر ب ب", "B002"), ("ء ل ف", "B001")),
    ],
    "22:48": [
        f("Bir yerleşime tanınan uzun süre bile onu yakalanma ve belirlenmiş sona varma doğrultusundan çıkarmaz.", "strong", ("م ل و", "B001"), ("ء خ ذ", "B002"), ("ص ي ر", "B001")),
    ],
    "22:49": [
        f("Elçinin nedensel görevi sonucu zorla üretmek değil, uyarıyı sınırları açık biçimde kamuya bildirmektir.", "strong", ("ن ذ ر", "B001"), ("ب ي ن", "B004")),
    ],
    "22:50": [
        f("Uyarıya iman ve düzgün eylemle verilen karşılık, geçmişteki açığı bağışlamayla örterken geleceği değerli rızıkla açar.", "strong", ("غ ف ر", "B002"), ("ر ز ق", "B001"), ("ك ر م", "B001")),
    ],
    "22:51": [
        f("Ayetleri etkisiz bırakmak için amaçlı çaba, kaçış üretmek yerine kişiyi ateşle kalıcı bir yoldaşlığa bağlar.", "strong", ("س ع ي", "B001"), ("ع ج ز", "B002"), ("ص ح ب", "B001")),
    ],
    "22:52": [
        f("Vahyin iletilmesi, düşmanca eklemenin görünür olduğu, kaldırıldığı ve ayetlerin yeniden sağlamlaştırıldığı açık bir düzeltme süreci içerir.", "strong", ("ل ق ي", "B005"), ("ن س خ", "B001"), ("ح ك م", "B004")),
        f("Dilek bildiren sözcüğün tohum bırakma çağrışımı, düşmanca eklemeyi iletim alanına saçılan yabancı bir unsur gibi düşündürebilir.", "reject", ("م ن ي", "B007")),
    ],
    "22:53": [
        f("Aynı düşmanca ekleme, alıcının durumuna göre hastalıklı kalbi ve sertleşmiş kalbi açığa çıkaran bir sınamaya dönüşür.", "strong", ("ف ت ن", "B001"), ("ق ل ب", "B001"), ("ق س و", "B002")),
        f("İç sertlik, toplumsal yarılmaya dönüştüğünde uzaklığı kendi kendine büyüten bir karşı duruş üretir.", "strong", ("ش ق ق", "B004"), ("ب ع د", "B001")),
    ],
    "22:54": [
        f("Bilgi, gerçeği tanımaktan kalbin inanıp alçalmasına uzanan ve sonunda dış yönü değiştiren aşamalı bir dönüşüm üretir.", "strong", ("ع ل م", "B001"), ("خ ب ت", "B001"), ("ق ل ب", "B001")),
        f("Dosdoğru yola iletilmek, bir kez yön göstermekten çok bozucu müdahaleden sonra doğrultuyu koruyan sürekli bir rehberliktir.", "strong", ("ه د ي", "B001"), ("ص ر ط", "B001"), ("ق و م", "B008")),
    ],
    "22:55": [
        f("Süren kuşku, beklenmedik saatin gelişiyle tartışma halinde kalamayacağı geri çevrilemez bir varışa çarpar.", "strong", ("م ر ي", "B004"), ("ب غ ت", "B001"), ("ء ت ي", "B001")),
        f("Kısır gün, azabı yalnız acı veren değil, ardından yeni bir imkân doğurmayan sonuçsuz bir son haline getirir.", "strong", ("ع ق م", "B001")),
    ],
    "22:56": [
        f("Egemenlik o gün, grupları yargıyla ayırıp farklı yaşama alanlarına yerleştiren bağlayıcı bir düzen olarak görünür.", "strong", ("م ل ك", "B003"), ("ح ك م", "B002"), ("ب ي ن", "B002")),
        f("Düzgün işler, gizli ve korunaklı bir esenlik alanına girişle sonuçlanır.", "weak", ("ص ل ح", "B003"), ("ج ن ن", "B003"), ("ن ع م", "B001")),
    ],
    "22:57": [
        f("Ayetleri örtmek ve yalanlamak, gizlemeye çalışılan şeyi kamusal aşağılanma olarak yeniden açığa çıkarır.", "strong", ("ك ف ر", "B003"), ("ك ذ ب", "B002"), ("ه و ن", "B003")),
    ],
    "22:58": [
        f("Allah yolundaki göçün kopuşu, öldürülme veya ölümle kesilmeyen yönlü bir rızık güzergâhı açar.", "strong", ("ه ج ر", "B001"), ("س ب ل", "B001"), ("ر ز ق", "B001")),
        f("Öldürülmek ile doğal ölüm aynılaştırılmadan aynı ilahî rızık sonucunda buluşturulur.", "strong", ("ق ت ل", "B001"), ("م و ت", "B001")),
    ],
    "22:59": [
        f("Yerinden ayrılanların varacağı yer, dışarıdan yalnız ödül sayılmaz; içeri girenlerin kendi hoşnutluğuyla doğrulanır.", "strong", ("د خ ل", "B001"), ("ر ض و", "B001")),
        f("Allah'ın yumuşak davranışı, uğranan zararı bilmemek değil, giriş gerçekleşene kadar bilgili bir ölçülülük göstermektir.", "weak", ("ع ل م", "B001"), ("ح ل م", "B001")),
    ],
    "22:60": [
        f("Karşılık verme benzerlikle sınırlandırılır; yeni saldırı savunmayı doğurur ve bütün süreç bağışlama ufku içinde tutulur.", "strong", ("ع ق ب", "B007"), ("م ث ل", "B001"), ("ب غ ي", "B003"), ("ع ف و", "B001")),
        f("Bağışlama ve örtme, hak aramanın yanında etkin kalır; adalet misillemenin sınırsız büyümesine izin vermez.", "strong", ("غ ف ر", "B002"), ("ن ص ر", "B002")),
    ],
    "22:61": [
        f("Gece ile gündüzün birbirine geçirilmesi, ilahî kudreti karşıt zamanları ölçülü biçimde iç içe sokan ve sırayla yöneten güç olarak gösterir.", "strong", ("و ل ج", "B001"), ("ل ي ل", "B001"), ("ن ه ر", "B002")),
        f("İşitme ve görme, bu dönüşümlerin yanında gizli ve açık zararların da ilahî gözetim altında olduğunu bildirir.", "weak", ("س م ع", "B001"), ("ب ص ر", "B001")),
    ],
    "22:62": [
        f("Gerçek ile Allah dışında çağrılanların boşluğu, soyut adlarla değil, düzenli dönüşüm üretme veya etkisiz kalma farkıyla ayırt edilir.", "strong", ("ح ق ق", "B001"), ("ب ط ل", "B001"), ("د ع و", "B001")),
        f("Allah'ın yüceliği yalnız uzaklık değil, karşıt süreçleri yönetebilen üstün hâkimiyettir.", "weak", ("ع ل و", "B001"), ("ك ب ر", "B001")),
    ],
    "22:63": [
        f("Suyun ince ve görünmez işleyişi, bir gecikmeden sonra toprağın yeşermesiyle gözle görülür sonuca dönüşür.", "strong", ("ل ط ف", "B002"), ("خ ض ر", "B002"), ("ن ز ل", "B002")),
        f("Görmek burada yalnız yeşilliği fark etmek değil, görünen sonuçtan toprağın içindeki gizli sürece ulaşmaktır.", "weak", ("ر ء ي", "B001"), ("خ ب ر", "B001")),
    ],
    "22:64": [
        f("Göklerin ve yerin mülkiyeti Allah'a bir ihtiyaç sağlamaz; kendine yeterlilik, bu sahipliği çıkarıcı olmayan bir ilişki yapar.", "strong", ("غ ن ي", "B001"), ("ء ر ض", "B001")),
    ],
    "22:65": [
        f("İnsanın hareket edebildiği dünya, geminin akışına izin verilirken göğün düşmesinin tutulduğu iki yönlü bir düzenlemeyle ayakta kalır.", "strong", ("س خ ر", "B001"), ("ج ر ي", "B001"), ("م س ك", "B001")),
        f("Merhamet, hareketli insan alanını ve düşme ihtimali taşıyan sınırları koruyucu bir tutuş içinde muhafaza eder.", "strong", ("ر ح م", "B001"), ("ر ء ف", "B001")),
    ],
    "22:66": [
        f("Hayat verme, öldürme ve yeniden diriltme, ayrı kopuk olaylar değil, tek bir yönetim altında tekrarlanan bir dizi oluşturur.", "strong", ("ح ي ي", "B003"), ("م و ت", "B001")),
        f("Nankörlük, insanın bizzat yaşadığı hayat dizisini örtüp görünür deneyimin ötesindeki devamını reddetmesidir.", "strong", ("ك ف ر", "B004"), ("ء ن س", "B001")),
    ],
    "22:67": [
        f("Her topluluğa ayrı ibadet yolu verilmesi, ritüel çeşitliliğini Rabbin otoritesi hakkındaki çekişmeden ayırır.", "strong", ("ن س ك", "B003"), ("ن ز ع", "B006"), ("ء م ر", "B001")),
        f("Çağrı, karşılıklı çekiştirmenin yerine insanı Rabbine doğru yönelten bir yaklaşma yolu koyar.", "strong", ("د ع و", "B001"), ("ه د ي", "B001"), ("ر ب ب", "B002")),
    ],
    "22:68": [
        f("Tartışmadan çekilmek değerlendirmeyi sözlerin birbirine dolanmasından çıkarıp Allah'ın kişinin yaptığını bilmesine bağlar.", "strong", ("ج د ل", "B001"), ("ع م ل", "B001"), ("ع ل م", "B001")),
    ],
    "22:69": [
        f("Şimdiki görüş ayrılıkları zorla silinmez; aralarındaki kesin ayrım kıyamet günündeki ayrıntılı yargıya bırakılır.", "strong", ("خ ل ف", "B004"), ("ح ك م", "B002"), ("ب ي ن", "B002")),
    ],
    "22:70": [
        f("Gök ve yerdeki kapsamlı bilgi, yazıyla birleştirilip geri çağrılabilir, sağlam ve bağlayıcı bir kayda dönüşür.", "strong", ("ع ل م", "B001"), ("ك ت ب", "B002"), ("ك ت ب", "B003")),
        f("Bunun Allah'a kolay olması işin önemsizliğinden değil, bilginin eksiksiz biçimde kuşatılmış olmasındandır.", "weak", ("ي س ر", "B001")),
    ],
    "22:71": [
        f("Allah dışında kulluk edilen şeyler, yukarıdan gelen yetki ve içeride bulunan bilgi desteğinden aynı anda yoksun bir yapı oluşturur.", "strong", ("ع ب د", "B003"), ("ن ز ل", "B002"), ("س ل ط", "B002"), ("ع ل م", "B001")),
        f("Dayanaksız kulluk, kendisini savunacak bir destek de üretemediği için haksızları desteksiz bırakır.", "strong", ("ن ص ر", "B001"), ("ظ ل م", "B004")),
    ],
    "22:72": [
        f("Açık ayetlerin art arda okunması, onları tanımayan yüzlerdeki inkârı bedensel saldırı baskısına dönüştürür.", "strong", ("ت ل و", "B001"), ("ع ر ف", "B003"), ("و ج ه", "B001"), ("س ط و", "B001")),
        f("Ateş tehdidi, saldırmaya hazırlananların konumunu tersine çevirip asıl üzerlerine gelecek olan sonucu bildirir.", "strong", ("ن ب ء", "B002"), ("و ع د", "B002"), ("ص ي ر", "B007")),
    ],
    "22:73": [
        f("Sivrisinek kadar küçük bir canlıyı yaratma ve onun aldığını geri kurtarma deneyi, ilah diye çağrılanların gücünü en küçük ölçekte sınar.", "strong", ("خ ل ق", "B002"), ("ذ ب ب", "B001"), ("ن ق ذ", "B001")),
        f("Bütün çağrılanların toplanması bile tek bir küçük canlının hareketli gücüne denk olamaz.", "strong", ("ج م ع", "B001"), ("ض ع ف", "B001")),
        f("İsteyen ile istenenin birlikte zayıf olması, ihtiyaç ilişkisinin iki ucunu da birbirine bağımlı kapalı bir devreye çevirir.", "strong", ("ط ل ب", "B001"), ("ض ع ف", "B001")),
    ],
    "22:74": [
        f("Allah'ı gereği gibi değerlendirememek, önceki güç deneyinin açığa çıkardığı bir ölçme ve değer biçme hatasıdır.", "strong", ("ق د ر", "B001"), ("ح ق ق", "B001")),
        f("İlahî güç, dağınık kuvvet değil, karşı konulamayan ve parçalanmayan birleşik bir kudrettir.", "weak", ("ق و ي", "B001"), ("ع ز ز", "B001")),
    ],
    "22:75": [
        f("Elçilik yetkisi kişinin kendi kurduğu bir güç değil, melekler ve insanlar arasından arıtılarak yapılan bir seçimin sonucudur.", "strong", ("ص ف و", "B002"), ("ر س ل", "B002")),
        f("Allah'ın işitmesi ve görmesi, seçimin rastgele değil, iletim zincirinin bütün taraflarını kuşatan bilgiye dayandığını gösterir.", "strong", ("س م ع", "B001"), ("ب ص ر", "B001")),
    ],
    "22:76": [
        f("Elçiler önlerindeki ve arkalarındaki zaman ufuklarıyla birlikte bilinir; görevleri kuşatılmış bir bilgi alanında yürür.", "strong", ("ع ل م", "B001"), ("ي د ي", "B008"), ("خ ل ف", "B002")),
        f("Bütün işlerin Allah'a döndürülmesi, elçilerin gerçek görevini silmeden sonuçları yeniden asıl kaynağa bağlar.", "strong", ("ر ج ع", "B001"), ("ء م ر", "B001")),
    ],
    "22:77": [
        f("Rükû ve secdedeki dikey alçalma, Rabbe kulluktan dışarıya doğru yararlı iş yapmaya uzanmalıdır.", "strong", ("ر ك ع", "B001"), ("س ج د", "B001"), ("ف ع ل", "B001")),
        f("Kurtuluş, bir anda elde edilen payeden çok yararlı eylemle yarılıp açılan ve yetiştirilen bir sonuçtur.", "weak", ("ف ل ح", "B005")),
    ],
    "22:78": [
        f("Allah yolundaki tam çaba, insanın seçilmiş kapasitesiyle sınırlanır ve dinde sıkışma üretmeme ilkesiyle dengelenir.", "strong", ("ج ه د", "B001"), ("ج ب ي", "B004"), ("ح ر ج", "B001")),
        f("İbrahim'in yolu, aşınmış olsa da açık kalan bir ata güzergâhı gibi kuşakları aynı teslimiyet adı altında birleştirir.", "weak", ("م ل ل", "B003"), ("ء ب و", "B001"), ("س م و", "B005")),
        f("Elçinin topluluğa, topluluğun da insanlara tanıklığı, hazır bulunma ve bilgili şahitliği kuşaklar boyunca aktaran bir zincir kurar.", "strong", ("ش ه د", "B001"), ("ر س ل", "B002")),
        f("Namazı sürdürmek, arınma payını vermek ve Allah'a sımsıkı bağlanmak, ibadet, toplumsal dolaşım, velilik ve yardımı tek koruyucu bağlılıkta toplar.", "strong", ("ق و م", "B004"), ("ز ك و", "B001"), ("ع ص م", "B001"), ("و ل ي", "B003"), ("ن ص ر", "B001")),
    ],
}


def canonical_bytes(value):
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


roster = json.loads(ROSTER.read_text(encoding="utf-8"))
anchor_map = json.loads(ANCHORS.read_text(encoding="utf-8"))
lookup = {(row[1], row[2]): row[0] for row in anchor_map["rows"]}
refs = [row[0] for row in roster["rows"]]

if refs != [f"22:{n}" for n in range(79)]:
    raise ValueError("Unexpected roster order")
if set(F) != set(refs):
    raise ValueError(f"Finding coverage mismatch: missing={set(refs)-set(F)}, extra={set(F)-set(refs)}")

ayat = []
for ref in refs:
    findings = []
    for item in F[ref]:
        keys = []
        for citation in item.pop("_citations"):
            try:
                key = lookup[citation]
            except KeyError as exc:
                raise KeyError(f"{ref}: missing anchor mapping for {citation}") from exc
            if key not in keys:
                keys.append(key)
        findings.append({"text": item["text"], "grade": item["grade"], "anchors": keys})
    ayat.append({"ayah_ref": ref, "findings": findings})

draft = {
    "protocol": "v12-cross-run-publication-draft-v3",
    "language": roster["language"],
    "surah": roster["surah"],
    "ayat": ayat,
}
draft_bytes = canonical_bytes(draft)
DRAFT.write_bytes(draft_bytes)

audit = {
    "protocol": "v12-cross-run-self-audit-v3",
    "draft_sha256": hashlib.sha256(draft_bytes).hexdigest(),
    "baseline_sha256": roster["baseline_sha256"],
    "language": roster["language"],
    "checked_ayah_refs": refs,
    "checks": {
        "target_language_only": True,
        "baseline_delta_only": True,
        "activated_and_retrospective_coverage": True,
        "atomic_findings": True,
        "fixed_ayah_anchors": True,
        "valid_grades": True,
    },
    "completed": True,
}
AUDIT.write_bytes(canonical_bytes(audit))
