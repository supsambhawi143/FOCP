{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ef5ea47d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total is 100\n"
     ]
    }
   ],
   "source": [
    "total = 100\n",
    "print(\"The total is\", total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d457b998",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total is now 199\n"
     ]
    }
   ],
   "source": [
    "total = total + 99\n",
    "print(\"The total is now\", total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8f632c0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total is 198\n",
      "The total is 792\n",
      "The total is 396.0\n"
     ]
    }
   ],
   "source": [
    "total -= 1\n",
    "print(\"The total is\", total)\n",
    "total *= 4\n",
    "print(\"The total is\", total)\n",
    "total /= 2\n",
    "print(\"The total is\", total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "396b8c03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average is 51.6\n"
     ]
    }
   ],
   "source": [
    "total = 98.2\n",
    "count = 5\n",
    "average = (total + count)/2\n",
    "print(\"Average is\", average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e05f2d47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n",
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'str'>\n",
      "<class 'bool'>\n",
      "<class 'float'>\n",
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(False))\n",
    "print(type(1000))\n",
    "print(type(100.111))\n",
    "print(type(\"Hello\"))\n",
    "print(type(True))\n",
    "print(type(100 / 5))\n",
    "print(type(100 // 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "80b022d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ABCABCABCABCABCABCABCABCABCABC'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"ABC\" * 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "13f475de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name: sambhawi\n",
      "Enter your address: ktm\n",
      "Enter your contact detail: xyz\n",
      "sambhawi\n",
      "ktm\n",
      "xyz\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name: \")\n",
    "address = input(\"Enter your address: \")\n",
    "contact = input(\"Enter your contact detail: \")\n",
    "print(name)\n",
    "print(address)\n",
    "print(contact)\n",
    "print(len(name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9c38b4f0",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_6608\\3180738729.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mage\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"Enter your age \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"in one year your age will be\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mage\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#This doesn't work because input function sets value data as string\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\anaconda\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1175\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1176\u001b[0m             )\n\u001b[1;32m-> 1177\u001b[1;33m         return self._input_request(\n\u001b[0m\u001b[0;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"shell\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\anaconda\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1217\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1218\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1219\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1220\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "age = input(\"Enter your age \")\n",
    "print(\"in one year your age will be\", age + 1)\n",
    "#This doesn't work because input function sets value data as string not an integer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b6ba08fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the first value: 4\n",
      "Enter the second value: 6\n",
      "Product of two numbers is 24\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter the first value: \"))\n",
    "b = int(input(\"Enter the second value: \"))\n",
    "product = a * b\n",
    "print(\"Product of two numbers is\", product)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d6d7bb11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I would have \"thought\" you knew better!\n"
     ]
    }
   ],
   "source": [
    "comment = 'I would have \"thought\" you knew better!'\n",
    "print(comment)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "14f5a9fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This text includes characters such as '\\' '\"' and \"'\",\n",
      "\tThis is a new line that starts with a tab\n",
      "\t\tThis new line starts with two tabs\n"
     ]
    }
   ],
   "source": [
    "print(\"This text includes characters such as '\\\\' '\\\"' and \\\"'\\\",\\n\\tThis is a new line that starts with a tab\\n\\t\\tThis new line starts with two tabs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b9c3728f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n",
      "Hello there!\n",
      "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n"
     ]
    }
   ],
   "source": [
    "print(\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \\nHello there!\\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "45473203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This text spans three lines,\n",
      "and includes both single ('),\n",
      "and double quotes (\").\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\"\"This text spans three lines,\n",
    "and includes both single ('),\n",
    "and double quotes (\").\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "58335a6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "l\n"
     ]
    }
   ],
   "source": [
    "surname = \"Palin\"\n",
    "initial = surname[0]\n",
    "third_letter = surname[2]\n",
    "print(third_letter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b5da3376",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "string index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_6608\\2509475999.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mtenth\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msurname\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtenth\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: string index out of range"
     ]
    }
   ],
   "source": [
    "tenth = surname[7]\n",
    "print (tenth)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "765aa7f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i\n"
     ]
    }
   ],
   "source": [
    "surname = \"Palin\"\n",
    "last = surname[-1]\n",
    "second_last = surname[-2]\n",
    "print(second_last)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "576fa0bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "alin\n"
     ]
    }
   ],
   "source": [
    "surname = \"Palin\"\n",
    "middle = surname[1:]\n",
    "print(middle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2b819664",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pali\n"
     ]
    }
   ],
   "source": [
    "surname = \"Palin\"\n",
    "a = surname[:4]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "aaa1a14c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 5, 7]\n"
     ]
    }
   ],
   "source": [
    "primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]\n",
    "print(primes[:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "64e43bb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Tim', 'Bill', 'John', 'Cena', 'Graeme']\n"
     ]
    }
   ],
   "source": [
    "names = [\"Tim\", \"Bill\", \"Graeme\"]\n",
    "names[2:2] = [\"John\", \"Cena\"]\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "7594ffed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "nums = [1,2,3] * 5\n",
    "print(nums)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
