import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

class QCY_FEATURE:

    @staticmethod
    def get_hog():
        from skimage import data, color, feature
        import skimage.data

        image = color.rgb2gray(data.coffee())
        hog_vec, hog_vis = feature.hog(image, visualise=True)

        fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(xticks=[], yticks=[]))
        ax[0].imshow(image, cmap='gray')
        ax[0].set_title('input image')

        ax[1].imshow(hog_vis)
        ax[1].set_title('visualization of HOG features')

        plt.show()

    @staticmethod
    def get_select():

        from sklearn.datasets import fetch_lfw_people
        faces = fetch_lfw_people(download_if_missing=True)
        positive_patches = faces.images
        positive_patches.shape

        from skimage import color, data, transform
        imgs_to_use = ['camera', 'text', 'coins', 'moon',
                    'page', 'clock', 'immunohistochemistry',
                    'chelsea', 'coffee', 'hubble_deep_field']
        images = [color.rgb2gray(getattr(data, name)()) for name in imgs_to_use]

        def extract_patches(img, N, scale=1.0, patch_size=positive_patches[0].shape):
            from sklearn.feature_extraction.image import PatchExtractor
            extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
            extractor = PatchExtractor(patch_size=extracted_patch_size, max_patches=N, random_state=0)
            patches = extractor.transform(img[np.newaxis])
            if scale != 1:
                patches = np.array([transform.resize(patch, patch_size) for patch in patches])
            return patches

        negative_patches = np.vstack([extract_patches(im, 1000, scale) for im in images for scale in [0.5, 1.0, 2.0]])
        negative_patches.shape

        fig, ax = plt.subplots(6, 10)
        for i, axi in enumerate(ax.flat):
            axi.imshow(negative_patches[500 * i], cmap='gray')
            axi.axis('off')

        plt.show()

    @staticmethod
    def get_result():
        from sklearn.datasets import fetch_lfw_people
        faces = fetch_lfw_people(download_if_missing=True)
        positive_patches = faces.images
        positive_patches.shape

        from skimage import color, data, transform, feature
        imgs_to_use = ['camera', 'text', 'coins', 'moon',
                    'page', 'clock', 'immunohistochemistry',
                    'chelsea', 'coffee', 'hubble_deep_field']
        images = [color.rgb2gray(getattr(data, name)()) for name in imgs_to_use]

        def extract_patches(img, N, scale=1.0, patch_size=positive_patches[0].shape):
            from sklearn.feature_extraction.image import PatchExtractor
            extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
            extractor = PatchExtractor(patch_size=extracted_patch_size, max_patches=N, random_state=0)
            patches = extractor.transform(img[np.newaxis])
            if scale != 1:
                patches = np.array([transform.resize(patch, patch_size) for patch in patches])
            return patches

        negative_patches = np.vstack([extract_patches(im, 1000, scale) for im in images for scale in [0.5, 1.0, 2.0]])
        negative_patches.shape

        from itertools import chain
        X_train = np.array([feature.hog(im)
                            for im in chain(positive_patches,
                                            negative_patches)])
        y_train = np.zeros(X_train.shape[0])
        y_train[:positive_patches.shape[0]] = 1
        X_train.shape

        from sklearn.svm import LinearSVC
        from sklearn.grid_search import GridSearchCV
        grid = GridSearchCV(LinearSVC(), {'C': [1.0, 2.0, 4.0, 8.0]})
        grid.fit(X_train, y_train)
        grid.best_score_

        grid.best_params_
        model = grid.best_estimator_
        model.fit(X_train, y_train)


        test_image = data.astronaut()
        test_image = color.rgb2gray(test_image)
        test_image = transform.rescale(test_image, 0.5)
        test_image = test_image[:160, 40:180]

        def sliding_window(img, patch_size=positive_patches[0].shape,
                   istep=2, jstep=2, scale=1.0):
            Ni, Nj = (int(scale * s) for s in patch_size)
            for i in range(0, img.shape[0] - Ni, istep):
                for j in range(0, img.shape[1] - Ni, jstep):
                    patch = img[i:i + Ni, j:j + Nj]
                    if scale != 1:
                        patch = transform.resize(patch, patch_size)
                    yield (i, j), patch
                    
        indices, patches = zip(*sliding_window(test_image))
        patches_hog = np.array([feature.hog(patch) for patch in patches])
        patches_hog.shape

        labels = model.predict(patches_hog)
        labels.sum()

        fig, ax = plt.subplots()
        ax.imshow(test_image, cmap='gray')
        ax.axis('off')

        Ni, Nj = positive_patches[0].shape
        indices = np.array(indices)

        for i, j in indices[labels == 1]:
            ax.add_patch(plt.Rectangle((j, i), Nj, Ni, edgecolor='red',
                                    alpha=0.3, lw=2, facecolor='none'))

        plt.show()