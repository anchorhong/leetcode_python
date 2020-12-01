from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        counter, res = Counter(S), list()
        arr = list(counter.keys())
        arr.sort(key=lambda x: counter[x], reverse=True)
        i, j = 0, 1
        while i < len(arr) and j < len(arr):
            t1, t2 = counter[arr[i]], counter[arr[j]]
            t = min(t1, t2)
            tmp = [arr[i], arr[j]] * t
            res.extend(tmp)
            counter[arr[i]] = counter[arr[i]] - t
            counter[arr[j]] = counter[arr[j]] - t
            i = max(i, j) + 1 if t1 <= t2 else i
            j = max(i, j) + 1 if t1 >= t2 else j
        if i < len(arr) and counter[arr[i]] == 1:
            res.append(arr[i])
        if j < len(arr) and 0 < counter[arr[j]]:
            n, k = counter[arr[j]], 0
            tmp = list()
            while n > 0 and k < len(res) and arr[j] != res[k]:
                tmp.extend([arr[j], res[k]])
                n -= 1
                k += 1
            if k < len(res) and tmp[-1] != res[k]:
                tmp.extend(res[k:])
            res = tmp

        return ''.join(res) if len(res) == len(S) else ""


if __name__ == "__main__":
    S = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
    print(Solution().reorganizeString(S))
