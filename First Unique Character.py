# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online




def moveZero[nums]
    zeroindex=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroindex] = nums[zeroindex], nums[i]
                zeroindex +=1
        return nums