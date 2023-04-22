#include <stdio.h>
#include <stdlib.h>
#define BLOCK_SIZE 2

// 16B / 2B = 8 cache sets
//set = 3
// offset = 1
// tag = 32 - 3 -1 = 28 tag bits
//  T   S  O 
// <28><3><1>

struct Set {
    unsigned char data[BLOCK_SIZE];
    unsigned int tag; // Assume tag is at most 32 bits
    unsigned char valid; // valid bit (0 or 1)
    };
struct Cache {
    struct Set *sets;
    int numSets;
};
unsigned int getOffset(unsigned int address) {
    // TODO – return unsigned-int value of offset bits from address
    // get the last bit in address
    return address & 0x1;

}
unsigned int getSet(unsigned int address) {
    // TODO – return unsigned-int value of set bits from address
    // shift the address right 1 and then get the last 3 bits
    return (address >> 1) & 0x7;
}
unsigned int getTag(unsigned int address) {
    // TODO – return unsigned-int value of tag bits from address
    //shift address right 4 to get tag bits
    return address >> 4;
}
struct Cache* mallocCache(int numSets) {
    // TODO - malloc a pointer to a struct Cache, malloc a pointer to an array
    // of struct Set instances (array length is numSets). Also initialize
    // valid to 0 for each struct Set. Return the struct Cache pointer.
    // malloc cache struct using sizeof to get length of the cache struct
    struct Cache* cache = malloc(sizeof(struct Cache));  
    //set numSets in the cache struct
    cache->numSets = numSets;  

    // malloc memory for pointer to a list of sets
    cache->sets = malloc(numSets * sizeof(struct Set));

    // loop through list of sets and set valid variable to zero
    for (int i = 0; i < numSets; i++) {
        cache->sets[i].valid = 0;
    }

    return cache;

}
void freeCache(struct Cache *cache) {
    free(cache->sets);
    free(cache);
}

void printSet(struct Set *set, int setIndex) {
    printf("set: %x - tag: %x - valid: %u - data:", setIndex, set->tag, set->valid);
    unsigned char *data = set->data;
    for (int i = 0; i < BLOCK_SIZE; ++i) {
        printf(" %.2x", data[i]);
    }
    printf("\n");
}   
void printCache(struct Cache *cache) {
    // TODO - print all valid sets in the cache.
    //loop through sets in the cache 
    for (int i = 0; i < cache->numSets; ++i) {
        //assign temp set struct to set i
        struct Set *set = &cache->sets[i];
        // if the set is a valid set than print the set ie did we put in anything at that set
        if (set->valid) {
            printSet(set, i);
        }
    }
}

void readValue(struct Cache *cache, unsigned int address) {
    // TODO - check the cache for a cached byte at the specified address.
    // If found, indicate a hit and print the byte. If not found, indicate
    // a miss due to either an invalid line (cold miss) or a tag mismatch
    // (conflict miss).
    //loop through sets in the cache
        printf("looking for set: %x - tag: %x\n", getSet(address), getTag(address));
        int is_valid = 0; // temp variable to check if there was a hit or miss
        for (int i = 0; i < cache->numSets; ++i) {
        struct Set *set = &cache->sets[i];
        //check if the set i is the same as the set in address
        if(set->valid & (getSet(address) == i)){
            is_valid = 2; // set is valid to a conflict miss. will change too hit if tags match
            //check if the address is valid and if the tag is the same.
            if (set->tag == getTag(address)) {
                //print the contents of the set 
                printf("found set: ");
                printSet(set, i);
                //print the offset value
                printf("hit: %x\n", set->data[getOffset(address)]);
                is_valid = 1;
            }

        }
        
    }
    //if there where no hits than declare a miss
    if(is_valid == 0){
        printf("no valid line found - miss!\n");
    }
    //if is_valid is 2 than sets match but tags don't so its a conflict miss. 
    if(is_valid == 2){
        printf("valid set found but tags don't match. conflict miss!\n");
    }

    


}
void writeValue(struct Cache *cache, unsigned int address, unsigned char *newData) {
    unsigned int s = getSet(address);
    unsigned int t = getTag(address);
    struct Set *set = &cache->sets[s];
    if (set->valid && set->tag != t) {
        unsigned char *data = set->data;
        printf("evicting line - ");
        printSet(set, s);
    }
    unsigned char *data = set->data;
    for (int i = 0; i < BLOCK_SIZE; ++i) {
        data[i] = newData[i];
    }
    set->tag = t;
    set->valid = 1;
    printf("wrote set: ");
    printSet(set, s);
}

unsigned int readUnsignedIntFromHex() {
    char buffer[10];
    char *p = NULL;
    unsigned int n;
    while (1) {
        fgets(buffer, sizeof(buffer), stdin);
        n = strtoul(buffer, &p, 16);
        if (buffer != p) {
            break;
        }
        printf("Invalid input - try again: ");
    }
    return n;
}
int main() {
    struct Cache *cache = mallocCache(8);
    char buffer[10];
    char c;
    do {
        printf("Enter 'r' for read, 'w' for write, 'p' to print, 'q' to quit: ");
        fgets(buffer, sizeof(buffer), stdin);
        c = buffer[0];
        if (c == 'r') {
            printf("Enter 32-bit unsigned hex address: ");
            unsigned int a = readUnsignedIntFromHex();
            readValue(cache, a);
        } else if (c == 'w') {
            printf("Enter 32-bit unsigned hex address: ");
            unsigned int a = readUnsignedIntFromHex();
            printf("Enter 32-bit unsigned hex value: ");
            unsigned int v = readUnsignedIntFromHex();
            unsigned char *data = (unsigned char *)&v;
            writeValue(cache, a, data);
            } else if (c == 'p') {
                printCache(cache);
        }
    } while (c != 'q');
    freeCache(cache);
}
