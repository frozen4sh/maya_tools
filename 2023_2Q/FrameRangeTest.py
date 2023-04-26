import maya.cmds as cmds
import pymel.core as pm



def getKeyframes(self,objs):
        
        all_key_frames = {}
        attr_list =[]
        time_list = []
        value_list =[]
        
        for obj in objs:
            anim_attr = pm.listAnimatable(obj)
            for attr in anim_attr:
                num_key_frames = pm.keyframe(attr,q=True,keyframeCount=True)
                if (num_key_frames > 0):
                    times = pm.keyframe(attr,q=True,index = (0,num_key_frames),timeChange=True)
                    values = pm.keyframe(attr,q=True,index = (0,num_key_frames),valueChange=True)
                    for i in range(0,num_key_frames):
                        
                        attr_list.append('%s'%attr)
                        time_list.append(times[i])
                        value_list.append(values[i])
        
        all_key_frames['Attribute'] = attr_list
        all_key_frames['Time'] = time_list
        all_key_frames['Value'] = value_list
        
        print (attr_list)
        print (time_list)
        print (value_list)
        
        return all_key_frames
    
