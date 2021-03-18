_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py', '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py'
]
model = dict(roi_head=dict(bbox_head=dict(num_classes=27)))
# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# actual epoch = 3 * 3 = 9
lr_config = dict(policy='step', step=[3])
# runtime settings
# total_epochs = 4  # actual epoch = 4 * 3 = 12


dataset_type = 'VOCDataset'
data_root = '/content/data/VOCdevkit/VOC2007'
data = dict(
    train=dict(
        dataset=dict(
            type='VOCDataset',
            ann_file = [
            "/content/data/Harshil/VOCdevkit/VOC2007/Main/train.txt",
            "/content/data/Tarun/VOCdevkit/VOC2007/Main/train.txt",
            "/content/data/Dhruv/VOCdevkit/VOC2007/Main/train.txt",
            "/content/data/Anjali/VOCdevkit/VOC2007/Main/train.txt",
            "/content/data/Pratik/VOCdevkit/VOC2007/Main/train.txt"],
            img_prefix =
            [
            "/content/data/Harshil/VOCdevkit/VOC2007",
            "/content/data/Tarun/VOCdevkit/VOC2007",
            "/content/data/Dhruv/VOCdevkit/VOC2007",
            "/content/data/Anjali/VOCdevkit/VOC2007",
            "/content/data/Pratik/VOCdevkit/VOC2007"],
            )),
    val=dict(
        type='VOCDataset',
            ann_file = "/content/data/Harshil/VOCdevkit/VOC2007/Main/val.txt",
            img_prefix = "/content/data/Harshil/VOCdevkit/VOC2007"
        ),
    test=dict(
        type='VOCDataset',
            ann_file = "/content/data/Harshil/VOCdevkit/VOC2007/Main/test.txt",
            img_prefix = "/content/data/Harshil/VOCdevkit/VOC2007"
        ))
total_epochs = 50
checkpoint_config = dict(interval=5)
