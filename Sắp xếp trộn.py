def merge_sort(arr):
    if len(arr) > 1:
        # chia danh sách thành 2 đoạn
        mid = len(arr) // 2
        # đoạn bên trái chạy từ phần tử đầu tiên đến phần giữa
        left_half = arr[:mid]
        # đoạn bên phải chạy từ phần giữa đến phần tử cuối cùng
        right_half = arr[mid:]
        # gọi đệ quy đoạn bên trái và bên phải để tiếp tục sắp xếp cho đến khi danh sách chỉ còn 1 phần tử
        merge_sort(left_half)
        merge_sort(right_half)

        # Sử dụng ba biến i, j và k để lặp qua left_half, right_half và arr
        i = j = k = 0

        # Thực hiện vòng lặp nếu i bé hơn số phần tử của đoạn trái và j bé hơn số phần tử đoạn phải
        while i < len(left_half) and j < len(right_half):
            # Nếu phần tử đầu tiên của đoạn trái bé hơn phần tử đầu tiên của đoạn phải
            if left_half[i] < right_half[j]:
                # Gán giá trị đầu tiên của danh sách cho giá trị i của đoạn trái
                arr[k] = left_half[i]
                # Và i lúc này sẽ tăng lên một đơn vị và cũng là giá trị đầu tiên của danh sách
                i += 1
            # Nếu phần tử đầu tiên của đoạn trái lớn hơn phần tử đầu tiên của đoạn phải
            else:
                # Gán giá trị đầu tiên của danh sách cho giá trị j của đoạn phải
                arr[k] = right_half[j]
                # Và j lúc này sẽ tăng lên một đơn vị và cũng là giá trị đầu tiên của danh sách
                j += 1
            # Tăng giá trị của k lên 1 đơn vị
            k += 1
        # Thực hiện vòng lặp nếu i bé hơn số phần tử của đoạn trái
        while i < len(left_half):
            # Thêm phần tử i của đoạn trái vào trong danh sách với vị trí k
            arr[k] = left_half[i]
            # đồng thời tăng i và k lên thêm 1 đơn vị
            i += 1
            k += 1
        # Thực hiện vòng lặp nếu j bé hơn số phần tử của đoạn phải
        while j < len(right_half):
            # Thêm phần tử j của đoạn phải vào trong danh sách với vị trí k
            arr[k] = right_half[j]
            # đồng thời tăng j và k lên thêm 1 đơn vị
            j += 1
            k += 1
    # Trả về danh sách đã được sắp xếp
    return arr

arr = [9,7,5,3,1,2,4,6,8]
print(merge_sort(arr))