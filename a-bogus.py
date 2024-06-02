import urllib.parse

import requests
import execjs

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'bd_ticket_guard_client_web_domain=2; live_use_vvc=%22false%22; xgplayer_user_id=330016342101; passport_assist_user=CkEMmPgBhsbuE2LkzCPw2BXUjr3nV5Yla59wJPUylICNA0hHzn467BEHsbG4sn79F6ZKbVZoKTRaAa9HaHEsyC839hpKCjxzmVSq4OGk3fp7glhQZ_aiqs0aah41L-VirJVgCs622NFbkdF8ifEI9l7vn-0WHmAEVH3D6tvSarPuCEcQuqfHDRiJr9ZUIAEiAQOiUl_K; sid_guard=6a0cefc693248930a3c3df93def1795c%7C1705885407%7C5184000%7CFri%2C+22-Mar-2024+01%3A03%3A27+GMT; store-region=cn-zj; store-region-src=uid; LOGIN_STATUS=1; my_rd=2; odin_tt=14697da7113db87dbcdda2a9a3039fd9e42e79b483f265ac279dfd3dd03f7d434cf5ab244360a3263e12b7abdb8573ebf6fe4032c809c79ea58dd151cde69ba7; ttwid=1%7CXypd9KaQGTxKjH_h9X6JTpp8zEoJpA-gkQPKLnc9I5w%7C1714290382%7C4d1a0928f4bf8cafd704fbd5eecbf7c2afaef779d360f693380cf8c6e04b6799; passport_csrf_token=ed720c9737cea15373ff9aeb4b9a7b3e; passport_csrf_token_default=ed720c9737cea15373ff9aeb4b9a7b3e; SEARCH_RESULT_LIST_TYPE=%22single%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; s_v_web_id=verify_lw7mtqv0_a687ZAZH_ctFj_4Ut4_AgDr_SLEu4pduXdKd; __live_version__=%221.1.2.139%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; csrf_session_id=998933618d7654d026be4afbd66dea4b; dy_swidth=1800; dy_sheight=1169; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1800%2C%5C%22screen_height%5C%22%3A1169%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.323%7D; pwa2=%220%7C0%7C1%7C0%22; download_guide=%223%2F20240526%2F1%22; __ac_nonce=0665b76e40019ce01b6df; __ac_signature=_02B4Z6wo00f01OEEKxAAAIDDs.sLCBALl-DhJC-AAF4g3DaLgKJjrEhjpvH-jQjBKarAVxqyrx45SxROJi3pwoApGKI7mu7gCM7PYIUTvOpRHDBnuAO82lT2faOmsMl0WJdsg36ef-cUrQSKb6; strategyABtestKey=%221717270246.519%22; xg_device_score=7.680383457615924; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQXVSZG5ISE9KZC8vSWlnV2ozY0dUTExYdHRvZTB2QWNwYTJWcndWMjBvdm1jbDhUUEV1dnFyMjg3QWlLOFp3YUthWjk4dDdxQWpvZG5VU1RGZmhQa0U9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=r-qLF0tLH0j2Hr6UqukVJjVGpRWo-Q0CygaP_0XyjqQMjoUXC-UFnIrIRG9K86x5-qkU_BjhvyVfwYnYnZ_MTbhtpsob6o_mMv2_eSdYdGelA3F_KTa3DXeB59sDgQ==',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAkeDX3Vsj5KqMVJnwzOEZ8U9VLA7DUiOSqMdkZ16gpS8?vid=7349872459904077067',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAkeDX3Vsj5KqMVJnwzOEZ8U9VLA7DUiOSqMdkZ16gpS8',
    'max_cursor': '1716200440000',
    'locate_item_id': '7349872459904077067',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '0',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1800',
    'screen_height': '1169',
    'browser_language': 'zh-CN',
    'browser_platform': 'MacIntel',
    'browser_name': 'Chrome',
    'browser_version': '124.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '124.0.0.0',
    'os_name': 'Mac OS',
    'os_version': '10.15.7',
    'cpu_core_num': '8',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7315820366097827366',
    'verifyFp': 'verify_lw7mtqv0_a687ZAZH_ctFj_4Ut4_AgDr_SLEu4pduXdKd',
    'fp': 'verify_lw7mtqv0_a687ZAZH_ctFj_4Ut4_AgDr_SLEu4pduXdKd',
    'msToken': 'M2JDIqM1aH21ov5wZsuasS3kBs8NNAmgaqRUWKscRUnjCEIP7eW0zkXB0DtftDr4smukE21WXjyvDvC9HjPirrhFnl6LlSh39v8aG19MrDeMq5uVc3UkCybxi6DUMA==',
}

params_str = urllib.parse.urlencode(params)

a_bogus = execjs.compile(open("a-bogus.js").read()).call("get_a_bogus", params_str)
print(a_bogus)
params['a_bogus'] = a_bogus

print(params)
response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', params=params, headers=headers)

print(response.text)

