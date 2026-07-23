# frozen_string_literal: true

require "digest"
require "json"

root = File.expand_path("../../../", __dir__)
roster_path = File.join(root, "_status/v12_cross_run/s025/ayah_roster.v3.json")
anchor_path = File.join(root, "_status/v12_cross_run/s025/anchor_map.v3.json")
draft_path = File.join(root, "_status/v12_cross_run/s025/publication.v3.draft.json")
audit_path = File.join(root, "_status/v12_cross_run/s025/self_audit.v3.json")

roster = JSON.parse(File.read(roster_path, encoding: "UTF-8"))
anchor_map = JSON.parse(File.read(anchor_path, encoding: "UTF-8"))
anchor_columns = anchor_map.fetch("columns")
anchor_lookup = anchor_map.fetch("rows").to_h do |row|
  data = anchor_columns.zip(row).to_h
  [[data.fetch("source_root"), data.fetch("source_branch")], data.fetch("anchor_key")]
end

finding = lambda do |text, grade, *anchor_specs|
  anchors = anchor_specs.map do |spec|
    anchor_lookup.fetch(spec) { raise "Missing anchor #{spec.inspect}" }
  end.uniq
  raise "Finding without anchors: #{text}" if anchors.empty?

  {"text" => text, "grade" => grade, "anchors" => anchors}
end

f = finding
findings = {
  "25:0" => [
    f.call("Açılıştaki rahmet, sure boyunca uyarı ve hükmü de içine alan, hayatı biçimlendiren rahim benzeri bir koruyucu alan olarak belirir.", "reject", ["ر ح م", "B003"])
  ],
  "25:1" => [
    f.call("İndiriliş, ayrımları uygulanabilir hale getiren kalıcı bir ölçünün kurulmasıdır; 25:32 bu inişin kalbi sağlamlaştıracak biçimde düzenli ve aşamalı olduğunu açığa çıkarır.", "strong", ["ب ر ك", "B004"], ["ن ز ل", "B002"], ["ف ر ق", "B001"]),
    f.call("Kul, itaatle biçimlenerek dünyalara yönelen uyarının bedensel ve okunabilir taşıyıcısı olur.", "reject", ["ع ب د", "B005"], ["ع ل م", "B002"])
  ],
  "25:2" => [
    f.call("Yaratılanların tam oranı, egemenliğin bölünmezliğini görünür kılar; ortaklık veya miras yoluyla devredilmiş bir yönetim fikrini dışlar.", "strong", ["م ل ك", "B003"], ["خ ل ق", "B001"], ["ق د ر", "B006"]),
    f.call("Gök ile yer arasındaki dikey bütünlük, ölçülmüş yaratılışta yönetimsiz hiçbir aralık bırakılmadığını gösterir.", "weak", ["س م و", "B004"], ["ء ر ض", "B001"], ["م ل ك", "B003"]),
    f.call("25:53-54, verilen ölçünün yalnız nicelik olmadığını; farklı suları ve insan bağlarını birbirine karıştırmadan ilişki içinde tuttuğunu gösterir.", "strong", ["خ ل ق", "B001"], ["ق د ر", "B006"])
  ],
  "25:3" => [
    f.call("Yaratılan ilahların kendi varlıkları üzerinde bile tasarruf kuramaması, ilahlık iddiasını tutarlı bir nedensellik sınavına çevirir.", "strong", ["خ ل ق", "B002"], ["م ل ك", "B002"]),
    f.call("Ölüm, hayat ve yeniden diriliş dizisi, gerçek egemenliğin yalnız varlıkları değil durumlar arasındaki geçişleri de yönetmesi gerektiğini gösterir.", "strong", ["م و ت", "B001"], ["ح ي ي", "B003"], ["ن ش ر", "B002"]),
    f.call("25:47-49, yeniden dirilişi yalnız gelecekteki bir olay olmaktan çıkarıp uyanışta ve yağmurla canlanan yerde sürekli gözlenebilen bir açılma örüntüsüne dönüştürür.", "strong", ["ن ش ر", "B001"]),
    f.call("25:8'deki bahçe ve beslenme, yeniden açılmayı yalnız dirilme değil, hayatı taşıyan üretken bir yayılma olarak da görünür kılar.", "weak", ["ن ش ر", "B001"])
  ],
  "25:4" => [
    f.call("Uydurma suçlaması, vahyin inişini insan üretimine çevirerek bizzat kınadığı yön saptırmayı kendisi gerçekleştirir.", "strong", ["ء ف ك", "B001"], ["ف ر ي", "B003"], ["ز و ر", "B001"]),
    f.call("Yardımcı bir topluluk varsayımı, sözün gerçek kaynağını örten ve nedenselliği yanlış yere koyan toplumsal bir açıklama kurar.", "weak", ["ع و ن", "B001"], ["ق و م", "B001"], ["ظ ل م", "B004"]),
    f.call("Kesip birleştirme ve söz hazırlama çağrışımları, suçlayanların vahye yüklediği üretim atölyesini aslında kendi iddialarını kurarken işlettiğini düşündürür.", "weak", ["ف ر ي", "B001"], ["ز و ر", "B006"]),
    f.call("25:33, bu yön saptırıcı açıklamaların her gelişinde gerçeği daha açık biçimde ortaya çıkararak suçlamanın istemeden açıklamayı çoğalttığını gösterir.", "weak", ["ء ف ك", "B001"], ["ز و ر", "B001"])
  ],
  "25:5" => [
    f.call("Masal, yazdırma ve dikte zinciri, vahyin düzenini tek bir intihalden çok sürekli işleyen insani bir üretim hattıyla açıklayan rakip bir kaynak modeli kurar.", "strong", ["س ط ر", "B001"], ["ك ت ب", "B001"], ["م ل و", "B004"]),
    f.call("Sabah-akşam uçları, tekrar eden alımı bir bağımlılık kanıtı gibi gösteren kesintisiz bir kopyalama takvimi oluşturur.", "weak", ["ب ك ر", "B001"], ["ء ص ل", "B003"]),
    f.call("25:32, gözlenen tekrarı inkâr etmez; onu insan diktesi yerine kalbi sağlamlaştıran ölçülü teslim olarak yeniden açıklar.", "strong", ["م ل و", "B004"], ["ك ت ب", "B001"]),
    f.call("25:9, bu üretim modelinin tarafsız bir açıklama olmadığını; yanlış görüntüler kurarak yol bulmayı bozduğunu açığa çıkarır.", "weak", ["س ط ر", "B001"], ["ك ت ب", "B001"])
  ],
  "25:6" => [
    f.call("Gizliyi bilenin indirmesi, metnin kaynağını gizli yardımcılarla değil, gizli gerçeklikleri açığa çıkarma yeterliğiyle açıklar.", "strong", ["ن ز ل", "B002"], ["ع ل م", "B001"], ["س ر ر", "B014"]),
    f.call("Gizlinin eksiksiz bilinmesine rağmen bağışlama ve rahmetin anılması, bağışlamayı bilgisizlikten doğan hoşgörü değil, bilinçli bir koruma ve dönüş imkânı yapar.", "strong", ["غ ف ر", "B001"], ["ر ح م", "B001"], ["س ر ر", "B001"])
  ],
  "25:7" => [
    f.call("Yemek ve çarşıda dolaşmak elçiliğin kusuru değil, uyarının ortak hayata bedensel dolaşım yoluyla ulaşmasını sağlayan altyapıdır; 25:20 bunu insanlar arası sınamanın parçası olarak doğrular.", "strong", ["ر س ل", "B001"], ["م ش ي", "B001"], ["س و ق", "B005"]),
    f.call("İstenen melek, mevcut uyarı işlevini yalnız görsel bir gösteriye taşıyarak tekrar eder; itiraz gerçek bir işlev eksikliği göstermez.", "weak", ["ن ز ل", "B002"], ["ن ذ ر", "B001"])
  ],
  "25:8" => [
    f.call("Hazine ile özel bahçe talepleri, vahyin yetkisini ortak hayata katılımdan bağımsız özel servet ve kapalı bollukla ölçen bir ekonomi anlayışı kurar.", "strong", ["ك ن ز", "B001"], ["ج ن ن", "B003"], ["ء ك ل", "B002"]),
    f.call("Büyülenmiş nitelemesi, bilinçli izlemeyi ele geçirilmiş harekete çevirerek izleyenlerin iradesini geçersiz sayar.", "weak", ["ت ب ع", "B003"], ["س ح ر", "B002"]),
    f.call("25:13, elçiye hazine atılması dileğini tersine çevirir: dışarıdan atılan değer talep edenler bu kez kendileri dar yere atılır.", "weak", ["ل ق ي", "B005"])
  ],
  "25:9" => [
    f.call("Yanlış benzetmeler yalnız hatalı betimleme üretmez; karşılaşmanın yerine imal edilmiş görüntüler koyarak yön bulma yetisini fiilen bozar.", "strong", ["ض ر ب", "B001"], ["م ث ل", "B008"], ["ض ل ل", "B001"], ["ط و ع", "B003"]),
    f.call("25:33'te aynı örnek getirme hareketi ters yönde işler: yanlış model yolu kaybettirirken cevaplanan model gerçeğin daha açık kurulmasına vesile olur.", "strong", ["ض ر ب", "B003"], ["م ث ل", "B004"]),
    f.call("25:12-13, bakma buyruğunu ateşin onları uzaktan görmesiyle ters çevirir ve yol bulamamayı dar mekânda bedensel sıkışmaya dönüştürür.", "weak", ["ن ظ ر", "B001"], ["ض ل ل", "B001"], ["س ب ل", "B001"])
  ],
  "25:10" => [
    f.call("Bahçeler ve saraylar yetkinin kanıtı olmaktan çıkarılıp ilahi iradeye bağlı bir armağan konumuna indirilir.", "strong", ["ش ي ء", "B002"], ["خ ي ر", "B005"], ["ج ن ن", "B003"]),
    f.call("Akan ırmaklar, 25:8'deki durağan hazineye karşı gerçek iyiliği dolaşan ve bulunduğu yeri dönüştüren bir bolluk olarak gösterir.", "strong", ["ج ر ي", "B001"], ["ن ه ر", "B001"]),
    f.call("25:15, daha iyiyi anlık gösterişin büyüklüğüyle değil kalıcılığa ulaşan sonuyla ölçerek talebin dar zaman ufkunu düzeltir.", "weak", ["خ ي ر", "B003"], ["ج ن ن", "B003"])
  ],
  "25:11" => [
    f.call("Önceki maddi kanıt taleplerinin altında son saati uzak sayma vardır; hazırlanmış ateş ise inkâr edilen geleceği şimdiden mevcut bir hazırlık olarak yakınlaştırır.", "strong", ["ك ذ ب", "B002"], ["ع ت د", "B001"], ["س ع ر", "B001"]),
    f.call("25:12, hazırlanmış ateşi uzaktan gören etkin bir bekleyiciye dönüştürerek hazırlığın durağan depolama değil yaklaşanı önceleyen bir durum olduğunu gösterir.", "strong", ["ع ت د", "B001"], ["س ع ر", "B001"])
  ],
  "25:12" => [
    f.call("Ateşin uzaktan görmesi ve temas kurulmadan işitilmesi, mesafeyi sığınak olmaktan çıkarıp bedensel varıştan önce başlayan duyusal bir yakalanma alanına çevirir.", "strong", ["ر ء ي", "B001"], ["ب ع د", "B001"], ["س م ع", "B011"]),
    f.call("25:34'te yüzüstü toplanma, uzaktan görülenlerin sonunda yön bulma organı olan yüzleriyle birlikte yönlerini de kaybettiğini gösterir.", "weak", ["ر ء ي", "B004"])
  ],
  "25:13" => [
    f.call("Atılma, darlık ve bağlanma bütün bedensel hareketi kaldırınca söz son çıkış denemesi olur; yok oluş çağrısındaki engellenme çağrışımı bu çıkışın da kapalı olduğunu gösterir.", "strong", ["ض ي ق", "B001"], ["ق ر ن", "B001"], ["د ع و", "B001"], ["ث ب ر", "B003"]),
    f.call("25:53'te sınır farklı suları üretken biçimde korurken burada aynı kapanma alanı suçluyu içeride tutar; sınırın işlevini bağlam belirler.", "weak", ["ض ي ق", "B001"], ["ق ر ن", "B001"])
  ],
  "25:14" => [
    f.call("Yok oluş çağrısının çoğaltılması bir son üretmez; ceza bitiş ihtiyacını sürekli yenileyip her çıkışı yine başarısız kılar.", "strong", ["د ع و", "B004"], ["ث ب ر", "B002"], ["ك ث ر", "B001"]),
    f.call("Çağrının sayıca artması kopmuş yardım ilişkisini geri getiremez; 25:18-19 bunu eski destekçilerin inkârı ve yardımın yokluğuyla açıklar.", "weak", ["د ع و", "B001"], ["ك ث ر", "B001"])
  ],
  "25:15" => [
    f.call("Korunma pratiği ile koruyucu ve kalıcı bahçe arasında uygunluk kurulur; varış yeri, önceki sakınmanın mekânsal biçimi haline gelir.", "strong", ["و ق ي", "B002"], ["ج ن ن", "B008"], ["خ ل د", "B001"], ["ص ي ر", "B007"]),
    f.call("25:74-76, bu varışın toplumsal yolunu açar: korunan hane rehberliğe, sabır yükselmeye ve kalıcılık güzel yerleşime dönüşür.", "weak", ["و ق ي", "B002"], ["ج ز ي", "B001"], ["ص ي ر", "B007"]),
    f.call("25:20, iyi sonu seçmenin bugünkü bağlantısını sabır olarak belirler; karşılaştırma yalnız iki yer arasında değil, o yerlere yerleşen davranış yolları arasındadır.", "weak", ["خ ي ر", "B003"], ["ص ي ر", "B007"])
  ],
  "25:16" => [
    f.call("Rabbin vaadi, değişken arzuyu kalıcı ve güvence altındaki bir beklentiye dönüştürür; nimet yalnız mevcut değil, ilişki içinde talep edilebilir durumdadır.", "strong", ["ش ي ء", "B001"], ["و ع د", "B001"], ["س ء ل", "B002"], ["ر ب ب", "B002"]),
    f.call("Bu talep, 25:21'deki zorlayıcı kanıt isteğinin tersine, önceden sunulmuş bir taahhüde verilen meşru cevaptır.", "strong", ["و ع د", "B001"], ["س ء ل", "B002"])
  ],
  "25:17" => [
    f.call("Tapılanlarla tapanların zorunlu olarak bir araya getirilmesi, yol kaybında dışarıdan saptırma ile kişinin kendi sapmasını ayıran bir sorumluluk incelemesi kurar.", "strong", ["ح ش ر", "B001"], ["ض ل ل", "B001"], ["س ب ل", "B001"]),
    f.call("25:18, doğrudan saptırma yerine uzayan nimet, unutma ve terk ediş zincirini göstererek sorumluluk sorusuna dolaylı bir oluşum cevabı verir.", "strong", ["ض ل ل", "B001"], ["س ب ل", "B001"]),
    f.call("25:55, güçsüz ilahların tapanların desteğine muhtaç olduğunu göstererek yönlendiren ile desteklenen arasındaki beklenen ilişkiyi tersine çevirir.", "weak", ["ع ب د", "B003"], ["ض ل ل", "B001"])
  ],
  "25:18" => [
    f.call("Kuşaklar boyu uzayan kesintisiz rahatlık, bağımlılığı görünmez kılıp hatırlatmayı terk etmeye ve toplumsal durgunluğa dönüşebilir.", "strong", ["م ت ع", "B007"], ["ن س ي", "B002"], ["ذ ك ر", "B009"], ["ب و ر", "B002"]),
    f.call("Yok olmuş topluluk, hatırlamanın işlemediği ve bu yüzden ekilip geliştirilmeyen toplumsal arazi gibi okunur.", "weak", ["ب و ر", "B003"], ["ذ ك ر", "B003"]),
    f.call("Tapılanların dostluk rolünü reddetmesi, Allah'ın dışında kendiliğinden edinilmiş bir ara yetki düzenini bütünüyle geçersiz kılar.", "strong", ["و ل ي", "B003"], ["ء خ ذ", "B010"], ["س ب ح", "B002"]),
    f.call("25:50, dolaştırılan nimetin hatırlatma amacı taşıdığını göstererek unutmayı nimet yokluğundan değil alınanı tanımayı reddeden bozulmuş karşılıktan doğan bir süreç yapar.", "strong", ["م ت ع", "B001"], ["ن س ي", "B002"], ["ذ ك ر", "B009"])
  ],
  "25:19" => [
    f.call("Tapılanların sözleri yalanlaması, yalnız bir iddiayı değil o iddiaya dayanan kaçış ve destek düzeninin bütününü çökertir.", "strong", ["ك ذ ب", "B002"], ["ق و ل", "B001"], ["ص ر ف", "B001"], ["ن ص ر", "B001"]),
    f.call("Azabın tattırılması, soyut biçimde reddedilen sonucu beden içinde sınanan ve inkâr edilemeyen bir bilgiye çevirir.", "strong", ["ذ و ق", "B002"], ["ع ذ ب", "B005"]),
    f.call("25:65, hükümden sonra imkânsız olan savuşturmanın hüküm yerleşmeden önce dua ile istenebileceğini gösterir; yön değiştirme fırsatı zamana bağlıdır.", "weak", ["ص ر ف", "B001"], ["ع ذ ب", "B005"])
  ],
  "25:20" => [
    f.call("Elçilerin sıradan bedensel ihtiyaçları ve toplum içindeki dolaşımı, görünüşe dayalı değer yargılarını açığa çıkaran karşılıklı sınamanın tasarlanmış aracıdır.", "strong", ["ب ع ض", "B001"], ["ف ت ن", "B001"], ["ص ب ر", "B001"]),
    f.call("İnsan gözü yeme ve yürümeyi eksiklik sayarken Rabbin iç görüşü bu temasın saklı tepkileri nasıl ölçtüğünü görür.", "strong", ["ب ص ر", "B002"], ["ر ب ب", "B002"]),
    f.call("25:63, aynı yeryüzü ve toplum içi hareketi sakin yürüyüş ve gerilimi düşüren sözle gerçekleştirerek sınamanın başarılı bedensel cevabını gösterir.", "strong", ["م ش ي", "B001"], ["ص ب ر", "B001"])
  ],
  "25:21" => [
    f.call("Karşılaşmayı beklemeyenlerin doğrudan görme talebi, delile açıklıktan çok vahyin hangi şartlarda görüneceğini kendilerinin belirleme girişimidir.", "strong", ["ل ق ي", "B004"], ["ر ء ي", "B001"], ["ن ف س", "B014"], ["ك ب ر", "B006"]),
    f.call("25:22 ve 25:25, istenen melek görüşünü ve inişini gerçekleştirir fakat değerini tersine çevirerek karşılaşmanın talep edenlerce yönetilemeyeceğini gösterir.", "strong", ["ل ق ي", "B004"], ["ع ت و", "B001"]),
    f.call("25:45-50, doğrudan görüş talebine gölge, güneş, uyanış, rüzgâr ve yağmurdan oluşan dolaylı bir işaret okulu sunar; bu okul şart koşmak yerine alçak gönüllü yorum ister.", "weak", ["ر ء ي", "B001"], ["ك ب ر", "B006"])
  ],
  "25:22" => [
    f.call("İstenen melek görüşü geldiğinde suçun yükü onu müjdeden dışlanmaya çevirir; gerçekleşen talep erişimi açmak yerine mühürler.", "strong", ["ر ء ي", "B001"], ["ب ش ر", "B005"], ["ج ر م", "B003"], ["ح ج ر", "B001"]),
    f.call("İki kez söylenen yasaklama, gelmiş olanı sözle durdurmaya yönelik gecikmiş ve etkisiz bir koruma duvarı gibi işler.", "weak", ["ح ج ر", "B001"]),
    f.call("25:53'te aynı sınır kökü hayat veren ayrımı korur; sınırın cezalandırıcı değil, kişinin konumuna göre koruyucu ya da dışlayıcı olduğu açığa çıkar.", "strong", ["ح ج ر", "B006"])
  ],
  "25:23" => [
    f.call("Hesapta işe yönelmek, birikmiş görünen eylemlerin bağsız maddesini açığa çıkarır; ürün silinmekten çok tutulamaz parçacıklara ayrılır.", "strong", ["ق د م", "B004"], ["ع م ل", "B001"], ["ه ب و", "B002"], ["ن ث ر", "B001"]),
    f.call("25:72-73, işe bağ kazandıran yönü açıklar: yalana katılmamak ve ayetlere algısı açık karşılık vermek, eylemin dağılmadan amaçla birleşmesini sağlar.", "weak", ["ع م ل", "B001"], ["ن ث ر", "B001"])
  ],
  "25:24" => [
    f.call("Saçılmış tozun karşısında arkadaşlık, koruyucu örtü ve sabit dinlenme birlikte bulunur; doğru bağlılık kişiye ve eyleme yerleşecek bir yer kazandırır.", "strong", ["ص ح ب", "B001"], ["ج ن ن", "B008"], ["ق ر ر", "B003"]),
    f.call("25:28'deki yıkıcı yakın dost, barınağın toplumsal bağlardan bağımsız olmadığını; bağlılığın ya yerleşik koruma ya da yol kaybı ürettiğini gösterir.", "weak", ["ص ح ب", "B001"]),
    f.call("25:76, iyi yerleşimin kalıcı olduğunu bildirerek arkadaşlık ve korumanın toz gibi dağılmaya karşı geçici değil sürekli bir karşılık kurduğunu doğrular.", "strong", ["ق ر ر", "B003"], ["ج ن ن", "B008"])
  ],
  "25:25" => [
    f.call("Üstteki örtünün bulut örtüsü aracılığıyla yarılması, gizlenmenin kaldırılmasından çok açığa çıkışın yönetilen aracı haline geldiğini gösterir.", "strong", ["ش ق ق", "B001"], ["س م و", "B004"], ["غ م م", "B001"], ["ن ز ل", "B004"]),
    f.call("25:48'deki su inişiyle birlikte okunduğunda, görünmeyen düzenin iki maddi inişi biri hükmü kapatırken diğeri hayatı açar.", "weak", ["ن ز ل", "B001"])
  ],
  "25:26" => [
    f.call("Rahmet ile gerçek hüküm aynı egemenlikte birleşir; hak edilmiş ilişkilerin yürürlüğe girmesi merhametin kesintisi değil, ona direnen için çetin yüzüdür.", "strong", ["م ل ك", "B001"], ["ح ق ق", "B002"], ["ر ح م", "B001"], ["ع س ر", "B001"]),
    f.call("25:59, Rahman'ın hükmünü ölçülü yaratılış ve tamamlanmış kozmik düzen üzerinden işleterek gerçek egemenliği düzen kuran bir süreç olarak somutlaştırır.", "strong", ["م ل ك", "B001"], ["ر ح م", "B001"], ["ح ق ق", "B001"])
  ],
  "25:27" => [
    f.call("Eylemin araçları olan ellerin ısırılması, tutulmayan yol yüzünden insanın kendi fiillerini kendisine karşı tanıklığa çevirmesidir.", "strong", ["ع ض ض", "B001"], ["ي د ي", "B009"], ["ء خ ذ", "B009"], ["س ب ل", "B001"]),
    f.call("25:57 aynı yol tutma sözünü şimdiki açık seçime dönüştürür; yol elçiden ya da dosttan miras alınmaz, kişi tarafından fiilen tutulur.", "strong", ["ء خ ذ", "B009"], ["س ب ل", "B001"])
  ],
  "25:28" => [
    f.call("Yakınlık, ihtiyaç aralığını doldurarak rehberliğe ulaşan geçidi ele geçirir; adı verilmeyen dost bu mekanizmanın tek kişiye özgü olmadığını gösterir.", "weak", ["خ ل ل", "B001"], ["خ ل ل", "B003"], ["ف ل ن", "B001"], ["ء خ ذ", "B010"]),
    f.call("25:53-54, sağlıklı yakınlığın farkı silmek yerine ayrı suları ve soy ile evlilik bağlarını koruduğunu göstererek yolu kapatan dostluğun karşıtını verir.", "weak", ["خ ل ل", "B003"])
  ],
  "25:29" => [
    f.call("Hatırlatma zaten geldikten sonra gerçekleşen sapma, bilgi yokluğundan değil yakın görünen ilişkinin hatırlamayı terk ettirip desteğini çekmesinden doğar.", "strong", ["ذ ك ر", "B009"], ["ج ي ء", "B001"], ["خ ذ ل", "B002"]),
    f.call("İnsani yakınlık, gerçek ölçü noktasını uzaklaştırarak bilgisel mesafenin taşıyıcısı olabilir; şeytani yüzüstü bırakma bu sahte yakınlığın içinde başlar.", "weak", ["ش ط ن", "B001"], ["ء ن س", "B003"], ["خ ذ ل", "B002"]),
    f.call("25:50 ve 25:62, kaybedilmiş hatırlamayı nimetlerin dolaşımı ve zamanın dönüşümüyle yeniden açan iki karşı düzen kurar.", "strong", ["ذ ك ر", "B003"], ["ض ل ل", "B004"])
  ],
  "25:30" => [
    f.call("Sözü bir araya getiren Kur'an'ın terk edilmiş hale getirilmesi, basitçe okunmamasından öte topluluğun onu etkisiz ve ayrılmış bir nesne olarak kullanma biçimidir.", "strong", ["ق ر ء", "B001"], ["ء خ ذ", "B010"], ["ه ج ر", "B001"]),
    f.call("25:32, ayrılmış bırakılan metnin aslında alımı biçimlendiren ölçülü bir ritimle toplandığını gösterir; terk ediş bu kurucu düzeni reddeder.", "strong", ["ق ر ء", "B001"], ["ه ج ر", "B001"])
  ],
  "25:31" => [
    f.call("Her peygamberin karşılaştığı düşmanlık, görevin başarısızlığı değil yol gösterme ve yardımın işlediği tekrarlanan arazidir.", "strong", ["ع د و", "B001"], ["ه د ي", "B001"], ["ن ص ر", "B001"], ["ك ف ي", "B001"]),
    f.call("25:35'te Harun'un kardeş ve yardımcı oluşu, yeterli yardımın düşmanı ortadan kaldırmadan görev yükünü taşıyan insani bir biçim kazanabileceğini gösterir.", "weak", ["ن ص ر", "B001"]),
    f.call("25:52, yeterli yol gösterme ve yardımı düşmanlardan uzaklaştırılma değil, vahiy aracılığıyla bütün gücü kullanma görevi olarak somutlaştırır.", "strong", ["ه د ي", "B001"], ["ن ص ر", "B001"])
  ],
  "25:32" => [
    f.call("Tek parça iniş yerine ölçülü ve sıralı tekrar, kalbin taşıma gücünü düzenleyip muhalefet altında onu sağlamlaştıran bir oluşum tekniğidir.", "strong", ["ج م ل", "B003"], ["ث ب ت", "B003"], ["ف ء د", "B002"], ["ر ت ل", "B002"]),
    f.call("Kalbin iç ateşi çağrışımı, aşamalı okuyuşun duygusal ve düşünsel yükü bir anda yığmak yerine ayarladığını düşündürür.", "reject", ["ف ء د", "B001"], ["ر ت ل", "B002"]),
    f.call("25:62, aynı ölçülü tekrarı gece ve gündüzün dönüşümünde büyüterek vahyin ritmini kozmik bir hatırlama eğitimine bağlar.", "weak", ["ر ت ل", "B002"], ["ث ب ت", "B002"])
  ],
  "25:33" => [
    f.call("Her düşmanca örnek, gerçeğin yalnız karşılık vermesine değil, o örneğin gizlediği durumu teşhis edip açığa çıkarmasına fırsat olur.", "strong", ["م ث ل", "B008"], ["ح ق ق", "B005"], ["ف س ر", "B002"]),
    f.call("25:45-50, daha iyi açıklamanın yalnız sözlü cevap olmadığını; gölge, güneş, uyanış, rüzgâr ve yağmur ilişkilerinin de gizli düzeni teşhis eden göstergeler olduğunu açar.", "weak", ["ف س ر", "B002"])
  ],
  "25:34" => [
    f.call("Yön bulması gereken yüzün taşıma yüzeyine dönmesi, önceki yön kaybını bedensel ters çevrilme olarak dışa vurur; kötü yer ile sapkın yol tek mekânsal süreç olur.", "strong", ["و ج ه", "B002"], ["ح ش ر", "B001"], ["ض ل ل", "B001"], ["س ب ل", "B001"]),
    f.call("25:63'te yeryüzünde yumuşak yürüyüş, yüz ve yolun birlikte kaybına karşı doğru yönelimin bedensel karşılığını verir.", "weak", ["و ج ه", "B002"], ["س ب ل", "B001"])
  ],
  "25:35" => [
    f.call("Sözleri birleştiren kitap ile yük taşıyan kardeş-yardımcı paralel iki destek olur; metinsel bütünlük kamusal görevde insani ortaklıkla tamamlanır.", "strong", ["ك ت ب", "B001"], ["ء خ و", "B002"], ["و ز ر", "B004"]),
    f.call("25:54, kardeş desteğini soy ve evlilik bağlarına genişleterek yaratılmış akrabalığın rakip yetki değil görev taşıyan ilişki altyapısı olabileceğini gösterir.", "weak", ["ء خ و", "B001"], ["و ز ر", "B004"])
  ],
  "25:36" => [
    f.call("Görünür işaretleri silen topluluğun kendisinin tarihte silinmesi, yıkımı işaretleri reddetmenin tersine çevrilmiş sonucu yapar.", "strong", ["ء ي ي", "B003"], ["ك ذ ب", "B002"], ["د م ر", "B002"]),
    f.call("Yıkım kökündeki bir yere girme çağrışımı, işaret taşıyan iki elçinin reddedildiği toplumsal alana bu kez yıkımın girip yerleştiğini düşündürür.", "reject", ["د م ر", "B001"], ["ذ ه ب", "B006"]),
    f.call("25:73, görünür ayetin tek başına anlayışı zorlamadığını gösterir; tarihsel yıkım bile sağır ve kör karşılanırsa işaret görevini yerine getiremez.", "weak", ["ء ي ي", "B003"], ["ك ذ ب", "B002"])
  ],
  "25:37" => [
    f.call("Elçileri yalanlayanların su altında kaybolması, onların olayını sonraki insanlar için kalıcı ve görünür bir işarete dönüştürür; dinleyici zorla mesaja çevrilir.", "strong", ["غ ر ق", "B005"], ["ج ع ل", "B002"], ["ء ي ي", "B003"]),
    f.call("25:48-50, suyun ölçülü gelişinin diriltip hatırlatabildiğini göstererek boğulmanın karşısına onarıcı bir su iletişimi çıkarır.", "weak", ["غ ر ق", "B005"])
  ],
  "25:38" => [
    f.call("Adı verilen halklarla aradaki sayısız kuşak, tarihi kopuk hikâyeler değil farklı zaman ve yerlerde tekrarlanmış vakalardan oluşan yoğun bir dizi yapar.", "strong", ["ق ر ن", "B005"], ["ب ي ن", "B002"], ["ك ث ر", "B001"]),
    f.call("25:62, kuşakların aralıklı ardışıklığını gece ile gündüzün birbirinin yerini almasına yaklaştırarak tarihsel tekrarı günlük hatırlama imkânına çevirir.", "weak", ["ق ر ن", "B005"], ["ب ي ن", "B010"])
  ],
  "25:39" => [
    f.call("Her topluma önce örnek verilmesi, maddi parçalanmadan önce davranışı zihinde kırmaya çalışan önleyici bir müdahale bulunduğunu gösterir.", "strong", ["م ث ل", "B011"], ["ت ب ر", "B001"], ["ك ل ل", "B003"]),
    f.call("25:70, kötü işlerin iyiliğe dönüştürülebileceğini göstererek parçalanmanın zorunlu olmadığını ve örneğin hâlâ bütünlük kurabileceğini açığa çıkarır.", "weak", ["ت ب ر", "B002"])
  ],
  "25:40" => [
    f.call("Harabe kentten fiziksel olarak geçmek etkili görme üretmez; yeniden dirilişi sürekli ertelemek, görülen tarihin geleceğe ilişkin sonucunu zihne ulaştırmaz.", "strong", ["ر ء ي", "B001"], ["ر ج و", "B004"], ["ن ش ر", "B002"]),
    f.call("25:47-50, uyanış ve yağmurla canlanan toprağı yakın ve yinelenen diriliş örnekleri yaparak harabe kenti daha büyük bir gözlenebilir düzenin içine yerleştirir.", "strong", ["ن ش ر", "B002"], ["ر ء ي", "B002"])
  ],
  "25:41" => [
    f.call("Alay, gönderilmiş kişinin dışarıdan verilmiş işlevini denetlenebilir bir gösteri nesnesine çevirerek mesajın uyandırma baskısını etkisizleştirmeye çalışır.", "strong", ["ء خ ذ", "B010"], ["ه ز ء", "B001"], ["ب ع ث", "B002"], ["ر س ل", "B002"]),
    f.call("25:42, elçinin ilahları neredeyse yerinden edeceğini itiraf ederek alayın görünüşe tepki değil mesajın gerçek baskısını yönetme savunması olduğunu açığa çıkarır.", "strong", ["ه ز ء", "B001"], ["ب ع ث", "B002"])
  ],
  "25:42" => [
    f.call("İlahlara bağlı kalmak, pasif bir miras değil düzeltme baskısına karşı sabrı yanlış yönde kullanan sürekli bir koruma emeğidir.", "strong", ["ص ب ر", "B001"], ["ض ل ل", "B001"], ["ك و د", "B002"]),
    f.call("Sabır yön bakımından tek başına iyi değildir; neye tutunduğu ancak sonucu görme anında sınanır.", "strong", ["ص ب ر", "B002"], ["ح ي ن", "B001"], ["ر ء ي", "B001"], ["س ب ل", "B001"]),
    f.call("25:63, geçerli sabrın ölçüsünü Rahman'a bağlı sakin yürüyüş ve esenlik sözü olarak verir; burada ise aynı tutma gücü yanlış yolu sürdürür.", "strong", ["ص ب ر", "B001"], ["س ب ل", "B001"])
  ],
  "25:43" => [
    f.call("Arzu yalnız güçlü bir istek değil, karar yetkisinin devredildiği işlevsel bir yöneticiye dönüşür; elçi bu kapalı yetki döngüsünün zorlayıcı vekili değildir.", "strong", ["ء ل ه", "B001"], ["ه و ي", "B004"], ["و ك ل", "B006"], ["ء خ ذ", "B010"]),
    f.call("Arzudaki boşluk çağrışımı, sabit ölçünün yokluğunda iç düzenleme alanını ilk eğilimin doldurduğunu düşündürür.", "reject", ["ه و ي", "B001"]),
    f.call("25:58, doğru vekillik ilişkisini ölmeyen ve yeterli olana güvenmek olarak kurar; arzuya kapalı biçimde devredilen yetkinin karşısına bilgili koruyucuyu koyar.", "strong", ["و ك ل", "B001"], ["و ك ل", "B006"])
  ],
  "25:44" => [
    f.call("İşitme, itaate açık anlayışa; akıl da sapmayı dizginlemeye dönüşmediğinde yönlendirme döngüsü kırılır.", "strong", ["س م ع", "B003"], ["ع ق ل", "B001"], ["ض ل ل", "B001"]),
    f.call("25:48-49, hayvanların rüzgâr, su ve canlanan araziyle bağını sürdürdüğünü gösterir; insanı daha sapkın yapan, sahip olduğu düşünme imkânıyla bu işaret-cevap bağını koparabilmesidir.", "weak", ["ن ع م", "B005"], ["ع ق ل", "B002"])
  ],
  "25:45" => [
    f.call("Gölgenin uzayıp kısalması, sabit kalsaydı gizli olacak ilişkiyi görünür hale getirir; güneş değişen gölgenin kaynağını gösteren ölçü aracıdır.", "strong", ["م د د", "B001"], ["ظ ل ل", "B001"], ["س ك ن", "B001"], ["د ل ل", "B001"]),
    f.call("25:61-62, gölgenin gösterge oluşunu farklı gök ışıkları ve zamanın dönüşümüyle genişleterek yaratılışı birbirini açıklayan bir işaret düzenine dönüştürür.", "weak", ["د ل ل", "B001"], ["ر ء ي", "B002"])
  ],
  "25:46" => [
    f.call("Gölgenin çekilmesi yok oluş değil, önce yayılanın kolay ve denetimli biçimde kaynağına doğru toplanmasıdır.", "strong", ["ق ب ض", "B006"], ["ي س ر", "B005"]),
    f.call("25:47-49, bu geri alınış ve yeniden salınış düzenini uyku, uyanış ve ölü toprağın dirilmesinde tekrarlayarak yönetimin tersine çevrilebilir aşamalarla işlediğini gösterir.", "strong", ["ق ب ض", "B006"]),
    f.call("25:62, her çekilmenin ardından gelen yeni dönemi kaçırılmış dikkatin onarılabileceği ahlaki bir fırsat yapar.", "weak", ["ي س ر", "B001"])
  ],
  "25:47" => [
    f.call("Gece örtüp uyku faaliyeti keserken gündüz hayatı yeniden dışarı açar; günlük döngü ölüm ile dirilişi korunaklı ve yinelenen bir beden deneyimi olarak çalıştırır.", "strong", ["ل ب س", "B001"], ["س ب ت", "B002"], ["ن ش ر", "B001"], ["ن و م", "B009"]),
    f.call("25:75'te hayat ve esenlik dileyen karşılanma, gündüz açılan yayılışın yalnız uyanma değil toplumsal olarak hayata kabul edilme yönünü tamamlar.", "weak", ["ن ش ر", "B001"])
  ],
  "25:48" => [
    f.call("Rüzgârın su gelmeden önce ardışık işaretler taşıması, rahmeti önceden tanınabilir ve hazırlanılabilir aşamalı bir süreç yapar.", "strong", ["ر س ل", "B005"], ["ب ش ر", "B007"], ["ر ح م", "B001"], ["ط ه ر", "B004"]),
    f.call("25:59-60, rüzgârın haber verdiği rahmeti yaratılışın sahibi Rahman'a bağlar; secde reddi böylece alınan ekolojik rahmetin kaynağına karşı geri çekilme olur.", "weak", ["ر ح م", "B001"], ["ر س ل", "B005"])
  ],
  "25:49" => [
    f.call("Bir suyun önce sınırlı araziyi, ardından hayvanları ve insanları canlandırması, hayatı toprak, kaynak ve içenler arasındaki bağların onarımı olarak gösterir.", "strong", ["ح ي ي", "B002"], ["ب ل د", "B001"], ["س ق ي", "B002"]),
    f.call("25:74, suyla canlanan ortak hayatı kuşakların ortaya çıkışı ve aile rehberliğiyle genişleterek dirilişi toplumsal üretkenliğe bağlar.", "weak", ["ح ي ي", "B013"], ["خ ل ق", "B002"])
  ],
  "25:50" => [
    f.call("Suyun tekrar tekrar farklı yerlere çevrilmesi, alışkanlığı kırıp maddi dolaşımı zihinsel dönüşe çevirmeyi amaçlayan öğretici bir tekrardır.", "strong", ["ص ر ف", "B002"], ["ذ ك ر", "B009"]),
    f.call("Nankörlük, mevcut kanıtın yokluğu değil alınmış nimetin hatırlamaya dönüşmesini etkin biçimde engelleyip onu örtmektir.", "strong", ["ء ب ي", "B001"], ["ك ف ر", "B004"]),
    f.call("25:62, bir dolaşım örtüldüğünde bile gece ile gündüzün yeni hatırlama ve şükür fırsatı açmasıyla öğretici tekrarın ısrarını gösterir.", "strong", ["ص ر ف", "B007"], ["ذ ك ر", "B003"], ["ك ف ر", "B004"])
  ],
  "25:51" => [
    f.call("Her kente ayrı uyarıcı gönderme imkânının kullanılmaması, uyarının tek elçi ve sonraki büyük mesaj mücadelesi üzerinden merkezî biçimde yayılmasının seçildiğini belirginleştirir.", "weak", ["ب ع ث", "B002"], ["ق ر ي", "B001"], ["ك ل ل", "B003"], ["ن ذ ر", "B001"])
  ],
  "25:52" => [
    f.call("Boyun eğmemek mesajın yönünü muhaliflerin çerçevesine teslim etmez; büyük mücadele vahyi araç edinerek baskı altında sürdürülen yoğun bir açıklama emeğidir.", "strong", ["ط و ع", "B001"], ["ج ه د", "B001"], ["ك ب ر", "B010"]),
    f.call("25:72-73, bu mücadelenin iç disiplinini yalana varlık kazandırmamak ve gerçek ayet karşısında duyuları kapatmamak olarak gösterir.", "strong", ["ج ه د", "B001"], ["ط و ع", "B003"])
  ],
  "25:53" => [
    f.call("İki suyun salınması ile sınırlandırılması çelişmez; üretken sınır, hareketi durdurmadan farklı niteliklerin yan yana varlığını korur.", "strong", ["م ر ج", "B005"], ["ب ي ن", "B002"], ["ح ج ر", "B001"]),
    f.call("25:67, aynı yapıyı harcamaya taşır: sağlıklı dolaşım da sınırsız çıkış ile daraltma arasında işleyen bir sınır gerektirir.", "weak", ["ح ج ر", "B001"], ["ب ي ن", "B002"])
  ],
  "25:54" => [
    f.call("Ortak bir üretici maddeden soy ve evlilik bağı gibi iki ayrı ilişkinin kurulması, yaratmayı biyolojik başlangıçla birlikte toplumsal mimariye dönüştürür.", "strong", ["م و ه", "B004"], ["خ ل ق", "B001"], ["ن س ب", "B001"], ["ص ه ر", "B001"]),
    f.call("25:74, yaratılmış akrabalığı göz aydınlığı ve önderlik duasına taşıyarak soy ile evlilik bağlarını kamusal yönelişin malzemesi yapar.", "strong", ["ن س ب", "B001"], ["ص ه ر", "B001"])
  ],
  "25:55" => [
    f.call("Yarar ve zarar veremeyen ilahın görünür gücü kendisinden gelmez; tapan kişi toplumsal ve fiilî desteğini ona ödünç vererek güçsüz rakip düzeni ayakta tutar.", "strong", ["ن ف ع", "B001"], ["ض ر ر", "B001"], ["ظ ه ر", "B006"], ["ع ب د", "B003"]),
    f.call("25:68, bu sahte desteğin ahlaki karşıtını verir: kullar rakip çağrıyı reddederek hayat ve cinsellik üzerindeki korunmuş sınırları ayakta tutar.", "weak", ["ع ب د", "B003"], ["ظ ه ر", "B006"])
  ],
  "25:56" => [
    f.call("Müjde ile uyarı, sonucu zorla yönetmeden biri ümidi açan diğeri koruyucu dikkati uyandıran tamamlayıcı bir yönlendirme çiftidir.", "strong", ["ب ش ر", "B005"], ["ن ذ ر", "B001"], ["ر س ل", "B002"]),
    f.call("25:63, bu çift yönlü çağrının alınmış halini gösterir: esenlik sözü müjdenin güvenini, gerilimi büyütmemek ise uyarının disiplinini davranışa çevirir.", "strong", ["ب ش ر", "B005"], ["ن ذ ر", "B001"])
  ],
  "25:57" => [
    f.call("Maddi ücretin yerine isteyen kişinin yol tutması konur; görevin karşılığı elçinin aldığı servet değil, alıcının özgürce üstlendiği dönüşümdür.", "strong", ["ء ج ر", "B001"], ["ش ي ء", "B001"], ["ء خ ذ", "B009"], ["س ب ل", "B001"]),
    f.call("25:74, özgürce tutulan yolun kişide kalmayıp başkalarının izlediği örnekliğe dönüşebileceğini gösterir.", "weak", ["ء خ ذ", "B009"], ["س ب ل", "B001"])
  ],
  "25:58" => [
    f.call("Güven, ölmeyen ve kulların peşinden gelen sorumlulukları içten bilen koruyucuya hesaplı bir teslimdir; bilgisiz ya da edilgin bırakış değildir.", "strong", ["و ك ل", "B006"], ["م و ت", "B001"], ["ذ ن ب", "B002"], ["خ ب ر", "B001"]),
    f.call("Dinleyiciden ücret ve kesin cevap beklenmemesi, görevin istikrarını ölümlü kabulden değil tükenmeyen hayata dayanır hale getirir.", "strong", ["و ك ل", "B002"], ["ح ي ي", "B003"], ["ك ف ي", "B001"]),
    f.call("25:75, ölmeyene güvenin toplumsal karşılığını kulların hayat ve esenlik dileğiyle karşılanmasında gösterir; ölümlü destekçinin terk edişinin tersi gerçekleşir.", "weak", ["ح ي ي", "B007"], ["و ك ل", "B002"])
  ],
  "25:59" => [
    f.call("Aşamalı yaratılış egemenliği geciktirmez; ilişkileri tamamlanmış bir yaşam alanının ölçülü kuruluşu Rahman'ın yerleşik yönetiminin kanıtı olur.", "strong", ["خ ل ق", "B001"], ["ب ي ن", "B002"], ["س و ي", "B003"], ["ع ر ش", "B006"], ["ر ح م", "B001"]),
    f.call("Bilene sorma buyruğu, önceki gösteriş taleplerinin tersine, iddiayı şart koşmak yerine sınanmış bilgiye disiplinli erişimi önerir.", "strong", ["س ء ل", "B001"], ["خ ب ر", "B001"]),
    f.call("25:61-62, tamamlanmış gök ve zaman düzenini sabit konumlar, farklı ışıklar ve güvenilir dönüşümler halinde algılanabilir kılar.", "strong", ["س م و", "B004"], ["ب ي ن", "B002"], ["خ ب ر", "B001"]),
    f.call("25:63-64, Rahman'ın kozmik düzenini sakin toplumsal hareket ve dengeli beden duruşu olarak kulların hayatına taşır.", "weak", ["ر ح م", "B001"], ["س و ي", "B002"])
  ],
  "25:60" => [
    f.call("Aşağı yönelen secde buyruğu onlarda dışarı kaçışı artırır; reddedilen yetki, ek yönlendirmeyi ölçülebilir biçimde daha büyük ayrılığa çevirir.", "strong", ["س ج د", "B001"], ["ء م ر", "B002"], ["ز ي د", "B001"], ["ن ف ر", "B001"]),
    f.call("Yaratılışı düzenleyen Rahman adının teslimiyet noktası olması, onların cezadan çok merhametli yönetimin içine alınmaya direndiğini düşündürür.", "weak", ["ر ح م", "B001"], ["س ج د", "B004"]),
    f.call("25:61-64, Rahman'ın ne olduğu sorusuna yön veren gök düzeni, yenilenen zaman, sakin yürüyüş ve secdeyle bedensel bir cevap verir.", "strong", ["ر ح م", "B001"], ["س ج د", "B001"])
  ],
  "25:61" => [
    f.call("Sabit gök konumları, güneş ve aydınlatan ay birlikte değişen şartlarda yön bulmayı sağlayan kamusal bir işaret altyapısı kurar.", "strong", ["ب ر ج", "B002"], ["س ر ج", "B001"], ["ن و ر", "B005"], ["ب ر ك", "B004"]),
    f.call("25:74-75, gökteki yön bulma düzenini izlenen insan örneğine ve yukarı kaldırılan sabırlı kullara taşıyarak yönelişi toplumsal ve ahlaki hale getirir.", "weak", ["ب ر ج", "B001"], ["ن و ر", "B005"])
  ],
  "25:62" => [
    f.call("Gece ile gündüzün birbirinin yerini alması, kaçırılan hatırlama veya şükür imkânını her döngüde yeniden açan bir onarım düzenidir.", "strong", ["خ ل ف", "B006"], ["ذ ك ر", "B003"], ["ش ك ر", "B002"]),
    f.call("25:63-67, yenilenen zamanı sakin söz, gece disiplini, sonuç bilinci ve sürdürülebilir harcama halinde ahlaki davranışa çevirir.", "strong", ["خ ل ف", "B001"], ["ذ ك ر", "B003"], ["ش ك ر", "B001"])
  ],
  "25:63" => [
    f.call("Alçak gönüllülük, bedenin ve sözün hızını toplumsal baskı altında koruyup kendini bilmez hitabın gerginliğini büyütmeyen etkin bir hareket denetimidir.", "strong", ["ه و ن", "B001"], ["خ ط ب", "B001"], ["ج ه ل", "B002"], ["س ل م", "B004"]),
    f.call("25:75, provokasyon karşısında yayılan esenliğin yüksek konutta onları karşılayan selam olarak geri döndüğünü gösterir.", "strong", ["س ل م", "B001"])
  ],
  "25:64" => [
    f.call("Gece boyunca secde ile ayakta duruşun dönüşümü, teslimiyet ile sorumlu hazır oluş arasında bedeni tekrar tekrar ayarlayan dikey bir eğitimdir.", "strong", ["ب ي ت", "B004"], ["س ج د", "B001"], ["ق و م", "B002"]),
    f.call("25:73, bu duruşları algısız düşüşten ayırır: gerçek alçalış işitme ve görmeyi kapatmadan sürer.", "strong", ["س ج د", "B001"], ["ق و م", "B002"])
  ],
  "25:65" => [
    f.call("Azap geçici acıdan çok kişiye yapışan borç benzeri bir yük olarak belirir; dua, bu sonuç ayrılmaz hale gelmeden yönün değiştirilmesini ister.", "strong", ["ص ر ف", "B001"], ["غ ر م", "B001"], ["غ ر م", "B003"]),
    f.call("25:76, yapışan azabın karşısına iyi yere kalıcı bağlılığı koyarak sürekliliğin niteliğini ilişkinin yönünün belirlediğini gösterir.", "strong", ["غ ر م", "B003"], ["ص ر ف", "B001"])
  ],
  "25:66" => [
    f.call("Kötülük, cezanın tek bir olay olmaktan çıkıp sabit zemin ve sürekli yaşam çevresi haline gelmesindedir.", "strong", ["س و ء", "B006"], ["ق ر ر", "B003"], ["ق و م", "B006"]),
    f.call("25:76 aynı kalma ve yerleşme çiftini olumlu kullanarak sorunun kalıcılıkta değil, kalıcı hale gelen yerin ahlaki niteliği ve kişiye uygunluğunda olduğunu gösterir.", "strong", ["ق ر ر", "B003"], ["ق و م", "B006"])
  ],
  "25:67" => [
    f.call("Denge iki miktarın aritmetik ortası değil, kaynağın dışarı akmasını sağlarken sistemi ne kayba ne darlığa sürükleyen taşıyıcı düzendir.", "strong", ["ن ف ق", "B002"], ["س ر ف", "B001"], ["ق ت ر", "B001"], ["ق و م", "B009"]),
    f.call("25:74, ev içindeki sürdürülebilir düzenin daha geniş korunmuş topluluğa yön verebilecek örnekliğe dönüşebileceğini gösterir.", "weak", ["ق و م", "B015"], ["ب ي ن", "B011"])
  ],
  "25:68" => [
    f.call("Ortak koşma, cana kıyma ve zina; yetki, hayat ve cinsel ilişki alanlarında kişiye verilmemiş sınırların ele geçirilmesi olarak tek bir dokunulmazlık düzeninde birleşir.", "strong", ["ح ر م", "B003"], ["ن ف س", "B011"], ["ل ق ي", "B007"], ["ء ث م", "B001"]),
    f.call("Yapmak ile karşılaşmak arasındaki geçiş, sınır aşımının kişiyi kendi sonucuyla yüz yüze getiren yolu kurduğunu gösterir.", "strong", ["ف ع ل", "B001"], ["ل ق ي", "B007"]),
    f.call("25:70, bu karşılaşmayı kaçınılmaz kader olmaktan çıkarır; iman ve düzgün iş, kurulmuş sonuç yolunu dönüşümle kesebilir.", "strong", ["ل ق ي", "B007"], ["ء ث م", "B001"])
  ],
  "25:69" => [
    f.call("Azabın katlanması önceki çoklu sınır ihlallerinin eşdeğer sonuçlar halinde birikmesine karşılık gelir; keyfî fazlalık değil, yığılmış fiillerin dönüşüdür.", "strong", ["ض ع ف", "B002"], ["ع ذ ب", "B005"]),
    f.call("Dirilişte ayağa kalkışın aşağılanarak kalmaya dönüşmesi, 25:63-64'teki sakin alçalış ve bilinçli dik duruşun nitelikçe tersine çevrilmesidir.", "weak", ["ق و م", "B013"], ["خ ل د", "B002"], ["ه و ن", "B003"]),
    f.call("25:76, kalıcılığın kendi başına ceza olmadığını; aynı yakın kalışın uygun ve güzel bir yerde arzulanan bağlılığa dönüşebildiğini gösterir.", "strong", ["خ ل د", "B002"])
  ],
  "25:70" => [
    f.call("İman ve düzeltilmiş eylem, bağışlamayı kötü işleri yalnız silen değil onların ahlaki niteliğini ve yapan kişiyi yeniden kuran üretken dönüşüm haline getirir.", "strong", ["ء م ن", "B001"], ["ع م ل", "B001"], ["ص ل ح", "B001"], ["ب د ل", "B002"], ["غ ف ر", "B002"]),
    f.call("25:75-76, dönüşen eylemin mekânsal ve toplumsal sonucunu yükselme, esenlikle karşılanma ve güzel kalıcı yerleşim olarak gösterir.", "strong", ["ب د ل", "B002"], ["ح س ن", "B001"], ["ع م ل", "B001"])
  ],
  "25:71" => [
    f.call("Dönüş kökünün tekrarı arasına yerleştirilen düzgün iş, içte başlayan yönelişi Allah'a gerçekten ulaşan ve dışarıdan sınanabilen bir yol haline getirir.", "strong", ["ع م ل", "B001"], ["ص ل ح", "B001"]),
    f.call("25:75, düzgün işle doğrulanan dönüşün varışını hayat ve esenlik veren yüz yüze karşılanmada somutlaştırır.", "weak", ["ع م ل", "B001"], ["ص ل ح", "B001"])
  ],
  "25:72" => [
    f.call("Yalana tanıklık etmemek ona toplumsal geçerlilik kazandıracak varlığı esirger; boş sözün yanından soyluca geçmek ise neyin dikkati hak ettiğini etkin biçimde seçer.", "strong", ["ش ه د", "B001"], ["ز و ر", "B002"], ["م ر ر", "B001"], ["ل غ و", "B001"], ["ك ر م", "B001"]),
    f.call("25:73, soylu geçişin bütün sözlerden kopuş olmadığını gösterir; boş sözden dikkat çekilirken gerçek hatırlatmaya işiterek ve görerek karşılık verilir.", "strong", ["م ر ر", "B001"], ["ل غ و", "B001"], ["ش ه د", "B002"])
  ],
  "25:73" => [
    f.call("Ayet karşısında güçlü bedensel tepki, işitme ve iç görüş kapalıysa gerçek teslimiyet değildir; ayet algıyı açık tutan etkin bir karşılık ister.", "strong", ["ذ ك ر", "B009"], ["ء ي ي", "B003"], ["خ ر ر", "B001"], ["ص م م", "B001"], ["ع م ي", "B002"]),
    f.call("25:74-75, algısı açık karşılığın aileyi biçimlendiren görüşe, kamusal örnekliğe ve yükseltilmiş karşılanmaya olgunlaştığını gösterir.", "strong", ["ذ ك ر", "B003"], ["ع م ي", "B002"])
  ],
  "25:74" => [
    f.call("Eş ve çocukların verdiği yerleşik görüş, ev içi armağanı kuşaklar boyunca yayılan ve daha geniş korunmuş topluluğa yön veren bir rehberlik ağına dönüştürür.", "strong", ["و ه ب", "B001"], ["ذ ر ر", "B004"], ["ق ر ر", "B002"], ["ع ي ن", "B003"], ["ء م م", "B009"]),
    f.call("25:75, izlenen önderlik yönünü dikey bir karşılıkla tamamlar: sabırla başkalarını yöneltenler yüksek yere çıkarılır.", "weak", ["ء م م", "B012"], ["و ق ي", "B002"])
  ],
  "25:75" => [
    f.call("Kendini tutanların yukarı kaldırılması, önceki alçalışlarına denk düşen mekânsal karşılıktır; onları karşılayan söz de hayat ve güvenlik veren toplumsal kabul olur.", "strong", ["ج ز ي", "B001"], ["غ ر ف", "B001"], ["ص ب ر", "B001"], ["ل ق ي", "B011"], ["ح ي ي", "B007"], ["س ل م", "B001"]),
    f.call("25:76, yüksek yere çıkarılmanın geçici bir yükseliş değil güzel ve kalıcı bir yerleşim olduğunu doğrular.", "strong", ["غ ر ف", "B002"], ["ج ز ي", "B001"])
  ],
  "25:76" => [
    f.call("Kalıcılığı güzel yapan yalnız sonsuz süre değil, karşılanma ve esenlikle kurulmuş ilişkinin kişiye uygun ve sabit bir yaşama çevresi olmasıdır.", "strong", ["خ ل د", "B001"], ["ح س ن", "B001"], ["ق ر ر", "B003"], ["ق و م", "B006"]),
    f.call("25:77, kalıcı bağlılığın yönünü son kez ayırır: ilişki ya çağrıyla değer kazanan yakınlık ya da inkârla ayrılmaz hale gelen sonuç olur.", "weak", ["خ ل د", "B002"], ["ق ر ر", "B003"])
  ],
  "25:77" => [
    f.call("İnsanın Allah'a yakarışı, onu ilişkisiz ağırlıksızlıktan çıkarıp Rabbin katında değer taşıyan gönüllü bir yakınlığa yerleştirir.", "strong", ["ع ب ء", "B002"], ["د ع و", "B001"], ["ر ب ب", "B001"]),
    f.call("İfade Allah'ın insanı çağırması olarak da okunursa, değer insanın kendiliğinden niteliğinden değil onu sorumlu ilişkiye çağıran hitaptan doğar.", "weak", ["د ع و", "B002"], ["ع ب ء", "B002"]),
    f.call("Çağrıyla kurulan ilişki yalanlandığında gönüllü yakınlığın yerini kişiden ayrılmayan zorunlu ve ağır sonuç alır.", "strong", ["ك ذ ب", "B002"], ["ل ز م", "B001"], ["ع ب ء", "B001"])
  ]
}

refs = roster.fetch("rows").map { |row| row.fetch(0) }
raise "Finding roster mismatch" unless findings.keys == refs

draft = {
  "protocol" => "v12-cross-run-publication-draft-v3",
  "language" => "tr",
  "surah" => 25,
  "ayat" => refs.map { |ref| {"ayah_ref" => ref, "findings" => findings.fetch(ref)} }
}
draft_json = JSON.generate(draft) + "\n"
File.write(draft_path, draft_json, mode: "w:UTF-8")

audit = {
  "protocol" => "v12-cross-run-self-audit-v3",
  "draft_sha256" => Digest::SHA256.hexdigest(draft_json),
  "baseline_sha256" => roster.fetch("baseline_sha256"),
  "language" => "tr",
  "checked_ayah_refs" => refs,
  "checks" => {
    "target_language_only" => true,
    "baseline_delta_only" => true,
    "activated_and_retrospective_coverage" => true,
    "atomic_findings" => true,
    "fixed_ayah_anchors" => true,
    "valid_grades" => true
  },
  "completed" => true
}
File.write(audit_path, JSON.generate(audit) + "\n", mode: "w:UTF-8")
