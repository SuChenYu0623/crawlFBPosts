import scrapy
import json
import time

import urllib.parse



class ExampleSpider(scrapy.Spider):
    name = "example"
    graph_url = "https://www.facebook.com/api/graphql/" # 改打 api

    # 最一開始直接複製 cookies, headers, payload 就好 (如果要自動化，要開瀏覽器去頁面拿)
    cookies = {
        "datr": "lFB0aHEDGv0Il2IDD5p2dgqu",
        "ps_l": "1",
        "ps_n": "1",
        "sb": "pVB0aEKs7cakFJ3PhHGP8g6D",
        "c_user": "61578362034790", # 身份驗證
        "xs": "22%3AXaeZJdrLv3UKXA%3A2%3A1752455745%3A-1%3A-1%3A%3AAcXSKGV-W1qHFAebYrfUh_18xyjHbB9bR3ERB2rpU2Q", # 身份驗證相關
        "fr": "1uIRP2QYqmpC4flzM.AWfiVT6pbrfWz6zwu3SIuakMLdSll8q6KfkwFXYSXsJCnUtAfLA.BodQRZ..AAA.0.0.BodQRZ.AWdiluZgzf7meIxyjdObi6D7AzQ",
        "wd": "1046x932",
        "presence": 'C{"t3":[],"utc3":1752456040337,"v":1}',
    }

    headers = {
        "accept": "*/*",
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.facebook.com",
        "referer": "https://www.facebook.com/groups/443709852472133?locale=zh_TW",
        "sec-ch-prefers-color-scheme": "light",
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.204", "Chromium";v="131.0.6778.204", "Not_A Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"6.8.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-asbd-id": "359341",
        "x-fb-friendly-name": "GroupsCometFeedRegularStoriesPaginationQuery",
        "x-fb-lsd": "f9-gUxblGwPI2mz3sATNey",
        "x-requested-with": "XMLHttpRequest",
    }

    raw_body = (
        "av=61578362034790&__aaid=0&__user=61578362034790&__a=1&__req=l&"
        "__hs=20283.HYP%3Acomet_pkg.2.1...0&dpr=1&__ccg=EXCELLENT&"
        "__rev=1024707914&__s=hjf16n%3A3wz8s7%3Ajt29cc&__hsi=7526744162955665267&"
        "__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE4u9x-3m1mzXw8W58jwGzEaE5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0-obUG2-azqwaW223908O3216xi4UK2K2WEjxK2B08-269wkopg6C13xecwBwWwjHBU-4EdrxG1fBG2-2K0E8460k-2K3aEy&__csr=hs5Ifgakj94Pinsr4T4iML6W9nslkyjqvn7OPaZvi48CIAGQx5lOZPRPbFuWZlqrkz-hlTheDkOGGkOlAqiVeQlQ8RBl4iZp9r-ht2plF5CqKKqbCFW9Lp6ECbBBGlkm8yriDBiAyAhkC4kW8bz9aTaqHyXXAhdrgK5kcyoTjXQ9GFEGnAy98gDyESEhVEiwImmqqhx2iaxG5HxS5p6QdDojgGmqm4o9pFohAyEGvgbEoxmu2m6E8qzoaUS8xfwCwFy45Ex0FDzVFESby89u2C7UGi1hxh7xK48hwi8SbzEnyUK6UCdzouJ0EwBwmo9FU985mdxl1m7ogwiEao2Dxq1yggjxq8h4UcE9o9o5-6U2Sw4-gsz-2Cbwt8nr81bg1RUoCxO0U8sgJ29Ud8coaFUrxO6E7m2GhbkOxl2E1Co2hhXjxm2SA2a0he2GqFQ4-azo8Erw9a2u5odN04-1hVQgwpy8co1L88U3pU04wq02ta9xS04A80grw51wMwQw0dBG0JPxG2_wFwu6E3eG1gw854Co9E6O0bH4WQQ02qy0hau9wdm1xy8C02Km0pekE0G28ykbDg1bU0S1w4ag1d4045Eao-0g-39w3Mk04ho0J0M1LU9Eqg0eTE7q8lweK0zk0OU0a8oy3vw7OK1Tw5BS&__hsdp=g8YfMu88gi86sOs4h2Ea9EqzH8lcV4hy4AjaaAgNVkFfci8Qgx4hcW4MMMWQz6h97XmCUD8bO9v4byOq8ppQEzhayqaQWrFzABjBiaIyW94uIhcGIP2WIs9V4UCeHb9LMojMvWGyy1yii13i6hj4UwGQaEEJBeOGBHuBWQGEReiHl89yUHg_hoCqiaF3UcEgzUiGAExkz26cy2KuA8zUJfx55gy9GiN5pF6iiirhzcEnylgEhPlDiBUBxjrAKO4eFnh912y2YHiSA64sHLOJ2d2F8gyHNyBAybKNOgwFiKl2ogKBoCbihyna6qJ2SN626WIMzKEyE-ayKbWgkxAWGoHzEkFx12Qi2bxhDy84ip2866cAyWJj6iE9G4osx28F5yEyezV8qDyWzXxJ0-xd2oa4EWi79U5eHoy12Bg4BNx8eaeU5JBa1rxJ0AwhQ3qQ1EBwzwzAw49yEnw4qx20CE4u5V8dAA22i9dxd0XwRh4qJ4NM3fwlWxx0ZwWxMipgy5GwNxy11S17wC8q1Iw5lzEdE12o2gwuW83a15xe2O4oaU4d06FyE0we260LU1U81fo2_wGw8G0_8Sdw40geE4mi9weO3m1owbe1uwtrwa64o727o1zU1ME6C3O0oW09-w7JwoE1ME2pw8S0mC1_xe4U&__hblp=0rm0J44oG3y3y360w8fE428xu7U0x-16xyewYwlHwvE23wlbyUS3OdCx94VUKcDwIwJzUrwQy8662C11xG2u18wywZwQwwy839xm1DweO4Q15wvqJy83zyo5O22exhd0zw863u3-2Sm2e2ei4U423q0E83nwgAu0C8C1vwMwRLCw8K18wno2DxO3S3G2i32Eco5HgS0S81lo1jU5Si7Ea8gw8C1pwIx62Ki1Qwa-8wKyE21wt84a0lq3K0CUC0H81cU5Kbwdmq0K8O7o2axim2u1rwwyoqwBzoaE24xK3h0Wwhp8C0_o985y2G0y84678eUerwa64o7248J0Ey824wzwbi1Rxa3u1uws85i3y2-6E561aw8-1xxC6E12EaU7K3p0nE3jy9Z90d6awAwoEK3Oi0wo3OwFwrU2cgcEK1jwbe4UW2-1fwDwh8e8nwBw&__comet_req=15&locale=zh_TW"
        "&fb_dtsg=NAfsInkYMzfK2JJJacMpgReFFBEmAYu64a2kty7XKqCOq0vv0b2gG2A%3A22%3A1752455745"
        "&jazoest=25410" # 藏在 script 內 (保持連線)
        "&lsd=Tcne2ABko0WDaQ2UkQU0CV" # 藏在 script (保持連線)
        "&__spin_r=1024707914"
        "&__spin_b=trunk"
        "&__spin_t=1752456688"
        "&__crn=comet.fbweb.CometGroupDiscussionRoute"
        "&qpl_active_flow_ids=431626709"
        "&fb_api_caller_class=RelayModern"
        "&fb_api_req_friendly_name=GroupsCometFeedRegularStoriesPaginationQuery"
        "&variables=%7B%22count%22%3A3%2C%22cursor%22%3A%22Cg8TZXhpc3RpbmdfdW5pdF9jb3VudAICDwtyZWFsX2N1cnNvcg%2BfQVFIUjZvZzl4OFpUaXdZYW9YWW9NZW13VlA4cnBWWEI2VEFEY1prNy02aFdXRlpMNDJqV21fUkVLbTNVMkVLdC1fUGJ0T1UtZzZaaUZ3dzVmQmJoQ2JZUFZnOmV5SXdJam94TnpVeU5EVTJOamc0TENJeElqbzNOamd5TENJeklqb3dMQ0kwSWpveExDSTFJam95TENJMklqb3dmUT09DxNoZWFkZXJfZ2xvYmFsX2NvdW50AgEPEm1haW5fZmVlZF9wb3NpdGlvbgICDw1mZWVkX29yZGVyaW5nDxtyYW5rZWRfaW50ZXJlc3RfY29tbXVuaXRpZXMPE2lzX2V2ZXJncmVlbl9jdXJzb3IRAA8iaXNfb2ZmbGluZV9hZ2dyZWdhdGVkX3Bvc3RzX2N1cnNvchEADxJncm91cF9mZWVkX3ZlcnNpb24PAlYyDxBkZW1vdGVkX3Bvc3RfaWRzCgEB%22%2C%22feedLocation%22%3A%22GROUP%22%2C%22feedType%22%3A%22DISCUSSION%22%2C%22feedbackSource%22%3A0%2C%22focusCommentID%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22group%22%2C%22scale%22%3A1%2C%22sortingSetting%22%3A%22TOP_POSTS%22%2C%22stream_initial_count%22%3A1%2C%22useDefaultActor%22%3Afalse%2C%22id%22%3A%22443709852472133%22%2C%22__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider%22%3Atrue%2C%22__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider%22%3Atrue%2C%22__relay_internal__pv__IsWorkUserrelayprovider%22%3Afalse%2C%22__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider%22%3Afalse%2C%22__relay_internal__pv__FeedDeepDiveTopicPillThreadViewEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider%22%3Afalse%2C%22__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider%22%3Afalse%2C%22__relay_internal__pv__IsMergQAPollsrelayprovider%22%3Afalse%2C%22__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider%22%3Atrue%2C%22__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometUFIShareActionMigrationrelayprovider%22%3Atrue%2C%22__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider%22%3Atrue%2C%22__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider%22%3Afalse%7D"
        "&server_timestamps=true"
        "&doc_id=30255376134109930"
    )
    
    raw_body = "av=61578362034790&__aaid=0&__user=61578362034790&__a=1&__req=n&__hs=20283.HYP%3Acomet_pkg.2.1...0&dpr=1&__ccg=EXCELLENT&__rev=1024713728&__s=a60tp5%3A3wz8s7%3A46tx27&__hsi=7526931343203380311&__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE4u9x-3m1mzXw8W58jwGzEaE5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0-obUG2-azqwaW223908O3216xi4UK2K2WEjxK2B08-269wkopg6C13xecwBwWwjHBU-4EdrxG1fBG2-2K0E8460k-2K3aEy&__csr=n1D3I2XbRtsahcJlkA4IjaIh8yTOayRPZhmGr9dvEJY9TbRi9spiYgqCWtRjridOurhtkRi-DdldH_bWAFlKtvhtrBytyd4WDuiaJ4ugKchABmAGmXFaFF9HhJaidLBh9e8Dz9pQszhp9KuHWgi_gio--jXiBGujGDAiBzoDCh8hhQubABwSCADhpUiCryVeaiQ224UuyotGpdu58S9jiKcjx22W5qypEGaxe6Unwzx52ohG6oiwxCwDxp3Uixm10xJGeBxe48CbxqbAz8Z0RCG1tz89e2u79Uy7Kq18wKBKu8BwSggxa4okz986i4ei6oboK2K3u0i64K4ocEW7Gxm7Usxa3632i1eG260BUdO2EhAw-z8qzo8WGAUCA26q3i1Bomwci0hq3O0i68950Lg27xW4o2eiU1So9k689U2Pxu0A8e8lz8Fei266VpU88cHgnw9e0i2foKXCwMwtHyoabxOi9G1JBwu85y1KCwa-017Qw0CTxe4U0iew11K0iJ1m00TuQ6EdFoug5W65FG0OqwOw8cwsUG2i1Jw2WhrFo09GU16u220RU4lw0Hyw6NOw2CAu9gK8w4Mw3o60gF04Tg0_Oawi816o89Q0f1g0gOw2Uj06IwYxx00XswtExm0WU2dg33w0ERgkxu0vWU6O0mYw&__hsdp=g8IcM8z1CwqiEdiEkg88Gax2EIJ8gAyCF9tEmiBgRyqiateAhC8Agy4E6TXAahqibp6ciDANyETrGbcHyoFepeH8zUBtpbcAtP9GQkBKBzeoy3a2a8wV2t84k4A2kW3qFms9844Q8N28VuqQr8BQbiFcjnAKJCGAsoBPAKu8GQmi9AIwCbAxGjAwxALyaQVQq5GCgV39bhri8F96mF4CKkMylDQ6kSWhpBrJbbYAUghUG-J5p4Ah4z64aYjh5R8Hi9aAoiAyhF6GgRq8h5Gh4G9x97gN4Qkqla8AEgjhku4pE-zBCqsFXgyt5omy4kiQy5BxeUMyBh45k2p1F6gd8eEhwGga6Foyay8bZmA6EUFEhawC2B6CzoOqimuicx6qu56UyayEF1S5oW2u13yS2Km12gtko5EcVubDa7u22iaw-wWohxgw5Oeg4V0jA48daQ17w87whawbO0zEa8N6eAP333Ey5A1nwIz8bU4hki2W1f81dw_6xWFNM4Wu6ok8by4u361tw59CwXxi2G0PE4uq3K10wda19wLzQ1rK5816U1081SU6YE5m0KudUK1fwfy0PU3uw4Gwl811UdVo10Etg5x060wwzE98a836wOxO0o-0M82zwd66981gEf8kwbC0Xo138qwcm1jxC0B898S0L83gw4jwae3i0YE39w7rwLw&__hblp=08Jwa6cgC2Kq3K2S1SwiEfob9E4u0pK2i1dwVDG1owMCwaK0yEK3a-4EcaAgrzUoBLxO1agOew8i2Gq3m2y1SG10x50Swq8G3y0D84S68dEG3-1WyQ2Om0xe78swVxi1qwceegQwfU4W48hwDwoo2oxqE760gC2ScCDg6m9yUsK1cwRDwmU8C1ewIxW260Xo5S0m61GwywaK9w8210wdamdwdaUkwbFa260jyE2sCw4Twg8622uU8o4m1dxDwko5G1owh81x42y0iau2aaw4KwZw42xR0m40ie1swwzE98a84e3y3y48mxK782iwp8fU5u0wEfp82uwFwGwt9UoAwJBwGz82byolgaoaEhxi1dwqU7i1Uw9y1PxG0NpXK-3S5GG2S1zwAzo2Iwdu8wu8fE3Dxu3i5o3dzE11U61wok3abwoodEkxG8-0jKUGqt2pE2Fw&__comet_req=15&locale=zh_TW&fb_dtsg=NAfsxxX5c5T62bZ_yZeFdDmtBxu9Gstu3cQ8l-Ftabsj4IIJqEBnq7Q%3A22%3A1752455745&jazoest=25580&lsd=-MdrGtOuzdD6iJutzDVmBj&__spin_r=1024713728&__spin_b=trunk&__spin_t=1752500269&__crn=comet.fbweb.CometGroupDiscussionRoute&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometFeedRegularStoriesPaginationQuery&variables=%7B%22count%22%3A3%2C%22cursor%22%3A%22Cg8TZXhpc3RpbmdfdW5pdF9jb3VudAICDwtyZWFsX2N1cnNvcg%2BfQVFIUjdITkVsZzR4VF90aDFGdHFZN2FvLU00bGl3eFdoSmRqQkZRVDlsWmRlMC1GWUxXUWl6Vkc0RkJhRXU4dTdYSmtoZlhiMnNsM1kwaVBjUF9RYzJsLW13OmV5SXdJam94TnpVeU5UQXdNamN3TENJeElqbzNOamd5TENJeklqb3dMQ0kwSWpveExDSTFJam95TENJMklqb3dmUT09DxNoZWFkZXJfZ2xvYmFsX2NvdW50AgEPEm1haW5fZmVlZF9wb3NpdGlvbgICDw1mZWVkX29yZGVyaW5nDxtyYW5rZWRfaW50ZXJlc3RfY29tbXVuaXRpZXMPE2lzX2V2ZXJncmVlbl9jdXJzb3IRAA8iaXNfb2ZmbGluZV9hZ2dyZWdhdGVkX3Bvc3RzX2N1cnNvchEADxJncm91cF9mZWVkX3ZlcnNpb24PAlYyDxBkZW1vdGVkX3Bvc3RfaWRzCgEB%22%2C%22feedLocation%22%3A%22GROUP%22%2C%22feedType%22%3A%22DISCUSSION%22%2C%22feedbackSource%22%3A0%2C%22focusCommentID%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22group%22%2C%22scale%22%3A1%2C%22sortingSetting%22%3A%22TOP_POSTS%22%2C%22stream_initial_count%22%3A1%2C%22useDefaultActor%22%3Afalse%2C%22id%22%3A%22443709852472133%22%2C%22__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider%22%3Atrue%2C%22__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider%22%3Atrue%2C%22__relay_internal__pv__IsWorkUserrelayprovider%22%3Afalse%2C%22__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider%22%3Afalse%2C%22__relay_internal__pv__FeedDeepDiveTopicPillThreadViewEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider%22%3Afalse%2C%22__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider%22%3Afalse%2C%22__relay_internal__pv__IsMergQAPollsrelayprovider%22%3Afalse%2C%22__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider%22%3Atrue%2C%22__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometUFIShareActionMigrationrelayprovider%22%3Atrue%2C%22__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider%22%3Atrue%2C%22__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=30255376134109930"

    # config
    page_count = 0
    page_limit = 1000
    time_range = 90 * 24 * 60 * 60 * 1000
    posts_data_list = []
    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.graph_url,
            method="POST",
            headers=self.headers,
            cookies=self.cookies,
            body=self.raw_body,
            callback=self.parse_api,
            dont_filter=True,
        )

    def parse_api(self, response):
        # 回傳的欄位包含 : 類型(主文/留言)、內容、時間、發文者/留言者。
        '''
        post_data = {
            "type": "主文/留言",
            "content": "內容",
            "post_time": "發文時間",
            "author": "留言者"
            "url": "連結 (方便我檢查)"
            "comments": [
                {
                    "content": "怎麽可能...",
                    "post_time": 1752419048000,
                    "author": "Nana Angler"
                }
            ]
        }
        '''
        # 固定
        print(f'\n=== 第{self.page_count}頁 parse api ===')
        self.page_count += 1
        text = response.text
        datas = text.split('\r\n')
        
        # 會發生變動的
        end_cursor = None
        insert = 0
        for data in datas:
            data = json.loads(data)
            if 'errors' in data.keys():
                print('errors', data['errors'])
                continue
            
            try:
                # 先拿翻頁
                if data['label'] == "GroupsCometFeedRegularStories_paginationGroup$defer$GroupsCometFeedRegularStories_group_group_feed$page_info":
                    if data['data']['page_info']['has_next_page']:
                        print(f'更新前 ====\n {end_cursor}')
                        end_cursor = data['data']['page_info']['end_cursor']
                        print(f'更新後 ====\n {end_cursor}')
                # 拿貼文內容
                elif data['label'] == "GroupsCometFeedRegularStories_paginationGroup$stream$GroupsCometFeedRegularStories_group_group_feed":
                    # 作者
                    author = data['data']['node']['actors'][0]['name']
                    # 貼文
                    content = ''
                    if data['data']['node']['comet_sections']['content']['story']['message']:
                        content = data['data']['node']['comet_sections']['content']['story']['message']['text']

                    # 發文時間
                    post_time = data['data']['node']['comet_sections']['timestamp']['story']['creation_time']

                    # 連結 (選)
                    url = data['data']['node']['comet_sections']['content']['story']['wwwURL']
                    
                    # 留言
                    comments = []
                    # 第一層留言 (時間因素，先只爬這裡，如果要向下挖，看起來小麻煩)
                    top_comments = data.get('data', {}) \
                        .get('node', {}) \
                        .get('comet_sections', {}) \
                        .get('feedback', {}) \
                        .get('story', {}) \
                        .get('story_ufi_container', {}) \
                        .get('story', {}) \
                        .get('feedback_context', {}) \
                        .get('interesting_top_level_comments', []) \
                                        
                    for top_comment in top_comments:
                        comment = top_comment.get('comment', {})
                        comment_author = comment.get('author', {}).get('name', '')
                        comment_content = comment.get('body', {}).get('text', '')
                        comment_post_time = comment.get('created_time', '')
                        
                        comments.append({
                            "content": comment_content,
                            "post_time": comment_post_time * 1000,
                            "author": comment_author
                        })

                    post_data = {
                        "type": "主文",
                        "content": content,
                        "post_time": post_time * 1000,
                        "author": author,
                        "url": url,
                        "comments": comments
                    }

                    # 過濾 90 天內 (約等於30天)
                    now_time = time.time() * 1000
                    if post_data['post_time'] >= now_time - self.time_range:
                        self.posts_data_list.append(post_data)
                        insert += 1

            except Exception as e:
                print('Err', e)
                pass
        print(f"--- 本輪增加了 {insert} 筆貼文資料 ---")
        time.sleep(2)

        # # 翻頁
        if self.page_count >= self.page_limit or insert == 0:
            end_task_reason = ''
            if self.page_count >= self.page_limit:
                end_task_reason = 'over page limut'
            elif insert == 0:
                end_task_reason = 'insert zero'
            else:
                end_task_reason = '不應該觸發，得修'
            print('工作結束原因:', end_task_reason)
            print('最後一頁:', self.page_count, self.page_limit)
            with open('output.json', 'w', encoding='utf-8') as f:
                json.dump(
                    self.posts_data_list, 
                    f, 
                    ensure_ascii=False,  # False 讓中文正常輸出，而不是 \uXXXX
                    indent=2
                )
            print('存檔')
        elif end_cursor:
            cursor_dict = {
                "count": 3,
                "cursor": end_cursor,  # 你要先定義好 end_cursor 這個變數
                "feedLocation": "GROUP",
                "feedType": "DISCUSSION",
                "feedbackSource": 0,
                "focusCommentID": None,
                "privacySelectorRenderLocation": "COMET_STREAM",
                "renderLocation": "group",
                "scale": 1,
                "sortingSetting": "TOP_POSTS",
                "stream_initial_count": 1,
                "useDefaultActor": False,
                "id": "443709852472133",
                "__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider": True,
                "__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider": True,
                "__relay_internal__pv__IsWorkUserrelayprovider": False,
                "__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider": True,
                "__relay_internal__pv__FeedDeepDiveTopicPillThreadViewEnabledrelayprovider": False,
                "__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider": False,
                "__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider": False,
                "__relay_internal__pv__IsMergQAPollsrelayprovider": False,
                "__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider": True,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False,
                "__relay_internal__pv__CometUFIShareActionMigrationrelayprovider": True,
                "__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider": False,
                "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider": True,
                "__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider": True
            }

            # 先把 dict 序列化成 JSON 字串
            json_str = json.dumps(cursor_dict, separators=(',', ':'))

            # 再做 percent-encoding，safe 參數對應 JS encodeURIComponent
            safe_chars = "-_.!~*'()"
            new_end_cursor = urllib.parse.quote(json_str, safe=safe_chars)
            
            self.raw_body = f"av=61578362034790&__aaid=0&__user=61578362034790&__a=1&__req=l&__hs=20283.HYP%3Acomet_pkg.2.1...0&dpr=1&__ccg=EXCELLENT&__rev=1024707914&__s=hjf16n%3A3wz8s7%3Ajt29cc&__hsi=7526744162955665267&__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE4u9x-3m1mzXw8W58jwGzEaE5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0-obUG2-azqwaW223908O3216xi4UK2K2WEjxK2B08-269wkopg6C13xecwBwWwjHBU-4EdrxG1fBG2-2K0E8460k-2K3aEy&__csr=hs5Ifgakj94Pinsr4T4iML6W9nslkyjqvn7OPaZvi48CIAGQx5lOZPRPbFuWZlqrkz-hlTheDkOGGkOlAqiVeQlQ8RBl4iZp9r-ht2plF5CqKKqbCFW9Lp6ECbBBGlkm8yriDBiAyAhkC4kW8bz9aTaqHyXXAhdrgK5kcyoTjXQ9GFEGnAy98gDyESEhVEiwImmqqhx2iaxG5HxS5p6QdDojgGmqm4o9pFohAyEGvgbEoxmu2m6E8qzoaUS8xfwCwFy45Ex0FDzVFESby89u2C7UGi1hxh7xK48hwi8SbzEnyUK6UCdzouJ0EwBwmo9FU985mdxl1m7ogwiEao2Dxq1yggjxq8h4UcE9o9o5-6U2Sw4-gsz-2Cbwt8nr81bg1RUoCxO0U8sgJ29Ud8coaFUrxO6E7m2GhbkOxl2E1Co2hhXjxm2SA2a0he2GqFQ4-azo8Erw9a2u5odN04-1hVQgwpy8co1L88U3pU04wq02ta9xS04A80grw51wMwQw0dBG0JPxG2_wFwu6E3eG1gw854Co9E6O0bH4WQQ02qy0hau9wdm1xy8C02Km0pekE0G28ykbDg1bU0S1w4ag1d4045Eao-0g-39w3Mk04ho0J0M1LU9Eqg0eTE7q8lweK0zk0OU0a8oy3vw7OK1Tw5BS&__hsdp=g8YfMu88gi86sOs4h2Ea9EqzH8lcV4hy4AjaaAgNVkFfci8Qgx4hcW4MMMWQz6h97XmCUD8bO9v4byOq8ppQEzhayqaQWrFzABjBiaIyW94uIhcGIP2WIs9V4UCeHb9LMojMvWGyy1yii13i6hj4UwGQaEEJBeOGBHuBWQGEReiHl89yUHg_hoCqiaF3UcEgzUiGAExkz26cy2KuA8zUJfx55gy9GiN5pF6iiirhzcEnylgEhPlDiBUBxjrAKO4eFnh912y2YHiSA64sHLOJ2d2F8gyHNyBAybKNOgwFiKl2ogKBoCbihyna6qJ2SN626WIMzKEyE-ayKbWgkxAWGoHzEkFx12Qi2bxhDy84ip2866cAyWJj6iE9G4osx28F5yEyezV8qDyWzXxJ0-xd2oa4EWi79U5eHoy12Bg4BNx8eaeU5JBa1rxJ0AwhQ3qQ1EBwzwzAw49yEnw4qx20CE4u5V8dAA22i9dxd0XwRh4qJ4NM3fwlWxx0ZwWxMipgy5GwNxy11S17wC8q1Iw5lzEdE12o2gwuW83a15xe2O4oaU4d06FyE0we260LU1U81fo2_wGw8G0_8Sdw40geE4mi9weO3m1owbe1uwtrwa64o727o1zU1ME6C3O0oW09-w7JwoE1ME2pw8S0mC1_xe4U&__hblp=0rm0J44oG3y3y360w8fE428xu7U0x-16xyewYwlHwvE23wlbyUS3OdCx94VUKcDwIwJzUrwQy8662C11xG2u18wywZwQwwy839xm1DweO4Q15wvqJy83zyo5O22exhd0zw863u3-2Sm2e2ei4U423q0E83nwgAu0C8C1vwMwRLCw8K18wno2DxO3S3G2i32Eco5HgS0S81lo1jU5Si7Ea8gw8C1pwIx62Ki1Qwa-8wKyE21wt84a0lq3K0CUC0H81cU5Kbwdmq0K8O7o2axim2u1rwwyoqwBzoaE24xK3h0Wwhp8C0_o985y2G0y84678eUerwa64o7248J0Ey824wzwbi1Rxa3u1uws85i3y2-6E561aw8-1xxC6E12EaU7K3p0nE3jy9Z90d6awAwoEK3Oi0wo3OwFwrU2cgcEK1jwbe4UW2-1fwDwh8e8nwBw&__comet_req=15&locale=zh_TW&fb_dtsg=NAfsInkYMzfK2JJJacMpgReFFBEmAYu64a2kty7XKqCOq0vv0b2gG2A%3A22%3A1752455745&jazoest=25410&lsd=Tcne2ABko0WDaQ2UkQU0CV&__spin_r=1024707914&__spin_b=trunk&__spin_t=1752456688&__crn=comet.fbweb.CometGroupDiscussionRoute&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometFeedRegularStoriesPaginationQuery&variables={new_end_cursor}&server_timestamps=true&doc_id=30255376134109930"
            yield scrapy.FormRequest(
                url=self.graph_url,
                method="POST",
                headers=self.headers,
                cookies=self.cookies,
                body=self.raw_body,
                callback=self.parse_api,
                dont_filter=True,
            )