1. `<:ramoke:1310422073562365972>` reaction when message contains `smok`
2. “right?” should work in the “@Pebble is this true?” thingy. say you say
   something, and in the next message go “@Pebble right?” — that should work
3. coin toss. if message contains “heads” of “tails”, will reply with heads or
   tails. example usage message: “@Pebble heads is rnote, tails is drawy”
4. @Pebble ping + word “rate” in message → replies with “n/10”, where n is an
   integer 0..=10

---

- Is message deferring neccessary?
- Allow the user who pinned the message to unpin
- Automatically unpin messages when the original message is deleted
- Timed-out users pinning permissions
- User cannot use context commands in channels with no send message permission
- Refactor everything
