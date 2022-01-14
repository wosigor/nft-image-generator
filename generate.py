#!/usr/bin/env python
# coding: utf-8

# In[35]:


from PIL import Image 
from IPython.display import display 
import random
import json
import os
import pprint


# In[36]:


path = "./trait-layers"
trait_directories = os.listdir(path)
trait_directories.remove(".DS_Store")
print(trait_directories)

trait_files = {}
for file in trait_directories:
    if file in trait_files:
        continue
    else:
        trait_files[file] = os.listdir(path + "/" + file)
        
for t in trait_files:
    trait_files[t].sort()
print(trait_files)


# In[49]:


# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

traits = {}

background = ['01.png', '01b.png', '01c.png', '02a.png', '02b.png', '02c.png', '03a.png', '03b.png', '03c.png']
background_weights = [10, 15, 15, 15, 15, 15, 5, 5, 5]

base = ['01a.png', '01b.png', '01c.png', '01d.png', '01e.png', '02a.png', '02b.png', '02c.png', '02d.png', '02e.png', '03a.png', '03b.png', '03c.png', '03d.png', '03e.png']
base_weights = [25, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

makeup = ['', '01.png', '02.png', '03.png', '04.png', '05.png']
makeup_weights = [40, 12, 12, 12, 12, 12]

eye = ['01.png', '02.png', '03.png', '04.png', '05.png']
eye_weights = [25, 20, 20, 20, 5]

hair = ['', '01a.png', '01b.png', '01c.png', '01d.png', '01e.png', '02a.png', '02b.png', '02c.png', '02d.png', '02e.png']
hair_weights = [70, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

hat = ['', '01a.png', '01b.png', '01c.png', '01d.png', '03a.png', '03b.png', '02.png', '03c.png', '03d.png', '03e.png']
hat_weights = [70, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

necklace = ['', '01.png', '02.png', '03a.png', '03b.png', '03c.png', '03d.png', '03e.png', '04a.png', '04b.png', '04c.png', '04d.png', '05a.png', '05b.png', '05c.png', '05d.png', '06a.png', '06b.png', '06c.png', '06d.png', '07a.png', '07b.png', '07c.png', '07d.png', '07e.png', '08a.png', '08b.png', '08c.png', '08d.png', '09a.png', '09b.png', '09c.png', '09d.png', '09e.png', '10a.png', '10b.png', '10c.png', '10d.png', '10e.png']
necklace_weights = [5, 0.5, 1, 1, 1.5, 1.5, 1.5, 1.5, 3.5, 3.5, 3.75, 3.75, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1.5, 1.5, 1.5, 1.5]

rings = ['', '01.png', '02.png', '03.png', '04.png', '05.png']
rings_weights = [50, 10, 10, 10, 10, 10]

sunglasses = ['', '01.png', '02a.png', '02b.png', '02c.png', '02d.png', '02e.png', '03.png', '04.png']
sunglasses_weights = [70, 4, 4, 4, 4, 4, 4, 4, 2]


# Dictionary variable for each trait. 
# Each trait corresponds to its file name

traits['background'] = background
traits['base'] = base
traits['makeup'] = makeup
traits['eye'] = eye
traits['hair'] = hair
traits['hat'] = hat
traits['necklace'] = necklace
traits['rings'] = rings
traits['sunglasses'] = sunglasses
print(traits)


directory_names = ['06_hat', '08_rings', '07_necklace', '03_makeup', '05_hair', '02_base', '04_eye', '01_background', '09_sunglasses']
directory_mappings = {}
for i, s in enumerate(directory_names):
    for t in traits.keys():
        if t in s:
              directory_mappings[t] = directory_names[i]
print(directory_mappings)
    


# In[ ]:





# In[50]:


## Generate Traits

TOTAL_IMAGES = 1000 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["background"] = random.choices(background, background_weights)[0]
    new_image ["base"] = random.choices(base, base_weights)[0]
    new_image ["makeup"] = random.choices(makeup, makeup_weights)[0]
    new_image ["eye"] = random.choices(eye, eye_weights)[0]
    new_image ["hair"] = random.choices(hair, hair_weights)[0]
    new_image ["hat"] = random.choices(hat, hat_weights)[0]
    new_image ["necklace"] = random.choices(necklace, necklace_weights)[0]
    new_image ["rings"] = random.choices(rings, rings_weights)[0]
    new_image ["sunglasses"] = random.choices(sunglasses, sunglasses_weights)[0]

    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)
    


# In[51]:


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))


# In[52]:


# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1


# In[53]:


print(all_images)


# In[54]:


# Get Trait Counts
trait_group_counts = {}
for img in all_images:
    print(img)
    break
    
for trait in traits:
    trait_group_counts[trait] = 0
    trait_counts = {}
    for trait_value in traits[trait]:
        trait_counts[trait_value] = 0
    trait_group_counts[trait] = trait_counts

    
print(trait_group_counts)

for image in all_images:
    for trait in trait_group_counts:
        trait_group_counts[trait][image[trait]] += 1
    
print(trait_group_counts)


# In[55]:


#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


# In[65]:



  
#### Generate Images    
for item in all_images:
  
  print(item)
  
  imgs = []
  for trait in item:
      if trait == 'tokenId':
          continue 
      # don't create images which have a blank option
      if item[trait] == '':
          continue
      img = Image.open(f'./trait-layers/{directory_mappings[trait]}/{item[trait]}').convert('RGBA')
#         img = img.resize((400,400),Image.ANTIALIAS)
      imgs.append(img)

  #Create each composite
  start_image = Image.alpha_composite(imgs[0], imgs[1])
  next_image = start_image
  for idx, val in enumerate(imgs):
      if idx < 2:
          continue
      else:
          next_image = Image.alpha_composite(start_image, imgs[idx])
          start_image = next_image

  #Convert to RGB
  rgb_im = next_image.convert('RGB')
  # resize images for sampling. Remove below line for final images
  smaller_img = rgb_im.resize((400,400),Image.ANTIALIAS)
  file_name = str(item["tokenId"]) + ".png"
  smaller_img.save("./images/" + file_name)
  
  


# In[63]:


#### Generate Metadata for each Image    

f = open('./metadata/all-traits.json',) 
data = json.load(f)


IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    for attr in i:
        token["attributes"].append(getAttribute(attr, i[attr]))

    print(token)
    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()


# In[ ]:





