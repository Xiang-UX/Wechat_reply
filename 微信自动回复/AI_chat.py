from zhipuai import ZhipuAI

conversation_history = {}
def zp_chat(nickname, last_msg):
    global conversation_history
    if last_msg == "清空":
        conversation_history[nickname][0].clear()
        a = "以清空对话"
        return a, nickname
    else:
        nicknames = {"role": "user", "content": last_msg}
        if nickname not in conversation_history:
            # 第一次对话
            conversation_history[nickname] = [
                {"role": "system",
                 "content": "你是一个可爱的智能小助理，风格偏萌妹，可以陪聊"},
                {"role": "system",
                 "content": "回复1至150字就行"},
                nicknames
            ],
        else:
            conversation_history[nickname][0].append(nicknames)
        messages = conversation_history[nickname][0]
        # print(messages)

        client = ZhipuAI(api_key="") 

        response = client.chat.completions.create(
            model="glm-4-plus", 
            messages=messages,
            max_tokens=300,
            top_p=0.2,
            temperature=0.4,

        )

        res = response.choices[0].message.content
        # print(f"[AI]:{res}")

        if res:
            messages.append({"role": "assistant", "content": res})
        # 回复
            return res
        else:
            res = "对话失败，请联系zx762857"
            return res
