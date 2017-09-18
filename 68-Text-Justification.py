class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        store = []
        line = []
        count, countword = 0,0
        while words:
            word = words[0]

            if count+len(word) <= maxWidth:
                count += len(word)+1
                countword += len(word)
                line.append(word)
                words.pop(0)
            else:
                store.append((line,countword))
                line = []
                count, countword = 0,0
        store.append((line,countword))

        #print store
        for i in range(len(store)):
            line,countword = store[i]
            if i == len(store)-1:
                temp = ' '.join(line)
                res.append(temp+' '*(maxWidth-len(temp)))
                continue
            if len(line)==1:
                res.append(line[0]+' '*(maxWidth-len(line[0])))
                continue
            spaces = len(line)-1
            spacenumber = ' '*((maxWidth-countword)/spaces)
            remain = (maxWidth-countword)%spaces
            print (maxWidth-countword)/spaces,(maxWidth-countword)%spaces
            for i in range(remain):
                line[i] = line[i]+' '

            res.append(spacenumber.join(line))
        return res


            
