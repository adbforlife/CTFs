import binascii
string = "826042ae444e454900000000b0b4263bedb0172e1ffbfeff961e210842632460788421098c9181e21084263242cd8696b93fd8a6e21084c648298ee5e986993d3d3ca6e2108513a8b98ee5e8a6e21084c648b98ee5e8a6e21084c648898ee5e8d6e2108507a8898ee5e8d6e21084c648c3f515fa60a8077108427dd42ec49300c56d207710842632411c772f4061a6cfe7f3e07710842632414c772f41f71084277d414c772f41f71084263244771dcbf3578ddc421098c9019c772ffa3c6ee21084c6487dc513af67bfc3771084263244d89c20ff127b8842135ea26c4e107f894af4fc2f97cbe6a71084c64845eb56ebc0c34c52bd2634905c2ff97f7d748149c42131921221dcbf1d849f936f45a7a7a7d83dec8e9c42131923dbc513f47cdf3ff8a578b4e90a30eb42ce210bec911de289e83f23da6021988edfe12ea9fa21097a961d257f7e63221dcbff46cf60f7d2c9220669e749362109269d478bf29817cc2b5dcd9ea6c658adb87e8abe91b36ef9378b0603442109e63a79fcac340c7be666cf7364afd273b15bfd3f63a9162e17ee2c180d108421996d0f2b0192dc2ba62d64a949cf80b7f3a7ec7522c1dd604f45c23a51d08ee2a6f621e094bbff4ce62e41a3ec4eb7b192ae572dfb3e5e5167a33010add5640a807f89b3b49994db251e907af0132b093d792dc91708e94741a88542c5141c7b94c71bc47ce2d78060f61907ec9f4cfdb969bf46a0175e728b48fb5fb63b1b016fcf4cc96b2551818ca03cafa0862e53706f6f9808e2baff9442fc6fe281e19bd265a1f8f03f64c45a45bffa5bbb625842811a759cdcf11e8adbccdbeaa63342c163234eed0dbaf00a9cc4b711cef77227896fcab225e5fc5442fc475cfcb9beb0b18d4df67a4337a4cb43f08061652dd481f8f49e686bd6c4cd9662aa1f1c40c05545b499082ff873ccf606652bb841ed57eb178e85831db37686dd780d6360d5e239d3d5c8d52cf5b0bc4dd659ac129ff4411aebc25e4ed738ef27c135f6873a591f62aab39bebc003302a4c6598e48a7ff7d92ac1291678f5465ea641d199bfeffbfbbddee2c77ddf77ed387b4a03326b477f75b7962f1d0b2c7b66ed33f875c8e166f3ceb8fb16ab0d5b19829f29c7e30bdeb29667460fa319d661a8d01a9302e01f0fceec8eb68771e329d18318a92cfd1c3d98b42a94b4b4a6533dd587f14459702d8237985f97e5fd7eb67ff81edc3b6f2c5e3a1658f6cd1a39a3fe88b107f14d9290d86c35315f592a9fcfd0bdeb29667460e0311d2c84df6376aca2a196ad902ca6c519b19a040659a2740c45ffb8a92ce6faf006cc713c6593ffb2b3127e50d01f05c6648465d521deecc358653db876de58bc742cb1ed9a344fac5cd1fc22c41fc530f5b3bc0baf0112d63365e81fc2b3979ab217bd63ac10d66aeb0595559ec0788cf97a341ad4c90980bbb4ace9b132b148cd293ec5aa87295f5a093a37892beeb391afd8afcc5a401f5a34410e20cfb52ac95d2619c5f9719817d993fc27e357549f673d7b207cc76de044f8e8580ecd8101b348fbc5ae6931125f7ea1d3ee229327a08f2b973e12f7cd9de61bb52658cd6a2a29ab217bd69ac3f74eb7701fe01e978b4bdc0133ad2becc778ad19a3ef1dc4f6082ce15880e0b3f8e59598a5277342ce94d38afcc83f6781d1a00d5b4fca559b15abcc8f0d519d5da770c6a90ece7af60958b3c18eb299bbaf0132b1c73d17546599d54faf169f966f055f98671a6bdd78d2850f477c6cb21b8384f79868d498e152f1988ab53560cbd7805d5859aaabc5b6a42e9325cdf8099d695de60058dcbd3af136ebc34e4f18b7dad1ca72b3686079dcb2063235f1a07c26d80f0cc4d95cad1a00d5b4fcb92ef32c51a2d00cd8342164c65d812ec73d7a5b23ed30bed8adfa65e38961c73d1754f7843ad356c342b3fef1d361091f5959e9e8787f561818278a64bf5e00a59c2aa8deb53563abeb6561bb6da074987b4167a49435470cc1cf31d83547d498eaf9028a6c061422c958464ceacb1c1d8d830274ccdb856571998043668ecf5a0d799e6ee5ef3208c6a34197576c89459edc018ad8332a5223ebdd930c201816e6d3d9957712cb4ea9ecc1ace3889460f4f06b0186ba603fef34a3b3dffcc8b18efc6fb0f7144b7883321c66f3186ada4c70af095bf728877b35d94b05ba0e45c7b1f8fc7c0db5217d7805966b7bd6c6660f02bebc004ac02847370f348c814fb10af091add598027d782b88e96c88ef995558247122c2e741af3265035cf8724cb72f0d421c7b7f018ad9eb647c3d77f93f5d1e6df2e7aee7782331dcacd90676cc05499671f1b3d7937149e8776531cdbc19869666ea4c0ba34c3dc65a7544b8094f66f312f86ebc5970cc5d651bdf0c9519588b095063fa41a4c0965e33367a513ef3f0bfe2bd4c4b9b2ec6ef652c376214d2de1e7608f18489fa86eeccd807172624e77855bdec6659b9a17293963bc53a6c905a98bfafebfaca400805d263218188a52a6860c0e4a54ef73bc1288ec66409d6c6a39f450561e460ecc3785afec277ac8d6bc77a263ed957fa240a2b695a30b8b41ad4c25af4870312209e9b5e60ccbb025d866ca7f304aa912d1671fef0e3499f32d68807c4a1f4b8c613b526365549ca6eebc01cac0efee2b5e7b1e68fa9f77666c016039d9e209f1d2a7e0e969fda224218b5a6da982565aafaaa44520eebc003302a4cb7edfb7d579d37ab5d68382c3af1e826b941677bcde094476b9e0234fca4072e0ac3c8c1d9bb4868cd8ed98bbc025aa18afd1316f6698f102ce8186bc518c1550b8b4c3d9d258de9d1f5e62ad1a2f31980575f155225a2dee607d688611333c7e50bb8044b352b64e2294caabc2b9e618d94da600c1396bf88d0584dcb0ebb401b43adeb425369cb4340256b0217b260ecd8f6af81e0f48b7530ae33063a5272f30d11ecc054980b96c1a0754cafa06cd9f9f9f79e26756820032a87b1ca58354fc2f97cbe34acc11ae0e75ba6cc2d024d2605c5a5b4c103012d4497553b931314dd124b7840a7a6dde18a3dc1cae2d0285ce86fb7d90a7e0b197798ab468bc966169fcfc4ddbe8cc4585bac7a686da98cc2077d144cf07f932a5e15c2d097a344b9b31cd6a8a3a82cfcf19bb454f1d468efa2cf41002eb232cb3326dc0df63356941f85ba980817c061ae38f17956edd984bc661fe7f9fe0643f1e75599daa2ef5e02056cdab63f1f8fed4581d296287fa5c36d9483c0363ad0944c7f1c2fb32202b41673aa724b425f54df476b4dc8817136ef13ae0789e366a2ec5695a42379878882b6f31568d178ccc2de19a43db7d1988b05b9670a19b94ef707cb04ad6f0b2f76805d9e266eea83185161416007d780966192ef7882bcc004ce5196599833499b87e2b8cc8726929f8b02867f1f57779868a749fb45a32502c87e20f5b59ad297b5429cc955a6323469cfa092d07b1b99d528385de64406a834a5b2937178ef2a7335dde40a9d28dc0d6a2ebee4699f3c7277ce9fc68d01a9318adf9568d179191ae236047b7d1994b05ba0e18ad904421fd56f9fb83eaa6555e145d68a8619e8f4cddcaa2c282c00faf012cc5decf553d20b53064ecbd27eec4d8c43509a1bbf5fb2335937a43a552126d986a262ae2ec6c2590eaf67a4aa3dd365ce4f7d4c6474d2659ba18812f21f03b538a4ae330754c880b26363ac8e49873c2a6a502a744f7c48e305e03330d87c081f260740fa9324fbcdb61d9861303372c0cfb464592c9251dfc47671f162c8b7551986a76c5c5167ec5d78926bffa5460d9b6685161416156e3a0e9a74ebe8b41f082246a3e26c1398c5ac7afb5b17e41cbff501b3264efbf7fbfde671aacddfac34c8ab36ccdf76e6f3f3f3fb3c00b88713772f408938f7d168afa0818096a2a0592f2395c660e4992fafc4dd8eb26c345a60d00baf011bb2f6b1d92d4aad4b81faa697a680812c6370d24cfedfd1577e778d53fef021ed4fc970cfd7f83dd9e839c7db7bd9c3d5a242bb1543e381ea74fa0c5a52b0a0b0496cf7618edf6fe1c67432b01e4c435099e8cc34b4f52f0efff65076a6074d925bccb5389607a71fbbb338e6b79f813cf82d0c14667b35d682debc0033535de7a1fbb67798d31df7c41a9b5e9a090da056e9c1fdb88de819868f66776a7e40e977d607bb3c530a6da14e1ee27b4a7284cd267bc1f75e00556a1dc54563c3d3433c746f11dad3a740be9e85e96c603c998b0d7d8ca0e5fa466978760f9d631a28ad78e498de65a9c4b0a31be85e612f198fb1966e68655bc9caef778cc1c930cf7c5333d003300bbdad066b1407eedcde1892d5aab56d4dae1bc6629d6fe0064ac758eaa8f0194f37f9650c2ad853f096971db3668277686d49963be0998273de3e2bfd16a72f72cd233d986743339e371cb45aa507e23b1b180f2662053ddeac65d25649ca0c1ede65a9c4b2c7aa7b32f75acf4b43a67a27cf716fdf632d360184273a6f3f92a3b0ecc0fddbfbc26c96ad55b2f71ca4a056c8ea3cb4650b9955ab69f84b4b8ed981304eed0da9301535ac7403b31bd35dda03d692e4978968a5c1cb66b520a8d8ad9182f4603c988620598278966103d4f660294aa8cc67cb1ae2796532c02e932e52128c69517434ac1f0f87e9507e53a354980c5e25e330aea5ee31598cdc710015b65569ad3f336971db302609dda55cb1dadb0b99e13c1c642b4645564ae8d69ac4b9b06b49805be4b01e4c20f16bc040ac7eedf7eb55022a83d19f2814ca7ffc38e61f71eab314a4e832d0624e57b5a926e5133a4c32b6115495379800fb66df0fdf5e0199aae5fe8a9ca6209e43ca1a1028778ebd8adf980f26347ae0538b043dbe9d9f2431990da69501af6627d3e9f8d6ab256ec18838cd8ed5f0446dd523bf96bc4a9bcc139b7cc8609d1a2c8d4883572fc277124c4227f301fcc20f16bc01b35293e319e92157faeabedd7bccc40ddb084c6df29cebe477198068cc6fdbf6fc61c34ad8593f4b0d98cc3c63598f5f6cfa913d013b1920be8ee2c0807e6347b63bfa46835d994a8a71be563d1b7d8baf71cddb853d184f0757c5754b61a956c339cd98cc3c63598f5f6cecd0e7a72bd8c90088d35e6764ac53880fa22cb8363b2b3225fcdbb0d4b84cffd318760cff3fcfeb613cf2f5e3663313632af19a7d999ad7ed183841bd8c9cde02bcd51e6de9c53727a006a1df66e0d8e6ac209eac66077e61ae9818096ef9df09ce75202c660077ef64dee930172c52280dca1f0f87d33df48a9e8a74b6dad3330c64e6f333885a1d6ceadf46b204ecdabdbac71d64d1ba58db6efb260573139d6ff8ae80c9d261cef805d4c12935887553acb67f9fe7ec257ca99eff8758ffb6cedb5bdfeff7d074a79ee887c4b30e263240acd22758aac9816ac8558a788478eb035d4c12935804e93208c0feb4ea7ad4fa7d3fe44e76f038bfc2a759604ef3694dbc26c87cd3103c4251acfd2c3675300ad6ff8b75978ac1d9604cde377e273d2d5a8eb035d4c127fcc127e20b3a9eb4d5ee0613ec840c9de61e6f96943e69816f15c1e2fa585a837017531b6b3cfd2dcc460a5aee4aeac1aea62773239adb3e7e7e78feb014c482cfab05aabec8805a641c43897a07cac5aeaf850956e9617ad607e1f87fe811cfccdce335647f1fc7e1aea601371fc6ebc5f93d5da4b64402d308e261f6af8fc5abad26f956d2c048a8125374bb90485886b4989b8fe293898c91c62154c61a08ab2beafabfdba3cf6960ba2c09561b6f4c4b0d4e95460916485291dbfab718a4a4e2632401c4c04995871e192b569e9e9fdaad1e6dbc21d0cc0491db9b235faf2bfafebfcfcfcfeffbfefcbce263243e884f32ffbfefff7fdff7c2f2acd7f5fd7de69d9b9215534de213192068854d13f4fd3f198096e7f3f9f1bb884263240d1091a27a7a78960294cee21098c903442d991225c0e779be6f9be3f8fe3f829c4213192303c421084c648c0f1084213192303c421084c648c0f1084213192303c421084c648c0f1084213192303c421084c648c0f1084213192303c421084c648c0f1084213192303c421084c648b0f10842109ff779e9ae924f73725492b725754fce67abba4aa92b73f93bbe74f7d7ce12023ec63c9011f722448912244adc4890e0912b95c8c03c112b9122448e57c51435249aaf9ded5e78544144492611000064a86fc701c30e0000c30e000073594870090000000561fc0b8fb10000414d416704000000e91cceae004247527301000000ee8d447a00000002085000000042020000524448490d0000000a1a0a0d474e5089"
print(len(string))
hexList = []
temp = ""
for i in range(len(string))[::-1]:
    if i % 2 == 0:
        temp = string[i] + temp
        hexList.append(temp)
        temp = ""
    else:
        temp = string[i] + temp
print(len(hexList))
hexListReversed = ""
for i in hexList:
    hexListReversed += str(i)
print(hexListReversed)
print(binascii.unhexlify(hexListReversed))
hex = open("/Users/ADB/Desktop/hex copy 3.txt", "w")
hex.write(binascii.unhexlify(hexListReversed))
hex.close()