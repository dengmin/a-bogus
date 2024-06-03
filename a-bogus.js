require("./env")
require("./bdms")

function get_a_bogus(p) {
    arguments = [
        0,
        1,
        14,
        p,
        "",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ]
    var r = window.dy._v;
    return (0, window.dy._u)(r[0], arguments, r[1], r[2], this)
}



console.log(get_a_bogus("device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAkeDX3Vsj5KqMVJnwzOEZ8U9VLA7DUiOSqMdkZ16gpS8&max_cursor=1716200440000&locate_item_id=7349872459904077067&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1800&screen_height=1169&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=124.0.0.0&browser_online=true&engine_name=Blink&engine_version=124.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7315820366097827366&verifyFp=verify_lw7mtqv0_a687ZAZH_ctFj_4Ut4_AgDr_SLEu4pduXdKd&fp=verify_lw7mtqv0_a687ZAZH_ctFj_4Ut4_AgDr_SLEu4pduXdKd&msToken=M2JDIqM1aH21ov5wZsuasS3kBs8NNAmgaqRUWKscRUnjCEIP7eW0zkXB0DtftDr4smukE21WXjyvDvC9HjPirrhFnl6LlSh39v8aG19MrDeMq5uVc3UkCybxi6DUMA%3D%3D"))
