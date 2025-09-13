# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

* Successful lookup: the element is in the filter.
* Unsuccessful lookup: the element is not in the filter, though lookup may return true.
* Mixed lookup: 10% successful, 90% unsuccessful.

For reference, we provide also insertion and lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.88</td>
    <td align="right">5.63</td>
    <td align="right">4.24</td>
    <td align="right">7.26</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.04</td>
    <td align="right">12.08</td>
    <td align="right">18.15</td>
    <td align="right">19.38</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.99</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">5.07</td>
    <td align="right">5.11</td>
    <td align="right">5.11</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.59</td>
    <td align="right">17.97</td>
    <td align="right">19.24</td>
    <td align="right">21.62</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.38</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.28</td>
    <td align="right">21.45</td>
    <td align="right">18.12</td>
    <td align="right">22.04</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.62</td>
    <td align="right">5.63</td>
    <td align="right">5.62</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.55</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.20</td>
    <td align="right">27.47</td>
    <td align="right">18.49</td>
    <td align="right">23.00</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.81</td>
    <td align="right">6.29</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.05</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.88</td>
    <td align="right">6.97</td>
    <td align="right">6.96</td>
    <td align="right">6.98</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.22</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">9.25</td>
    <td align="right">9.25</td>
    <td align="right">9.25</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.05</td>
    <td align="right">9.67</td>
    <td align="right">9.66</td>
    <td align="right">9.67</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.72</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.18</td>
    <td align="right">11.79</td>
    <td align="right">11.79</td>
    <td align="right">11.79</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.10</td>
    <td align="right">13.65</td>
    <td align="right">13.65</td>
    <td align="right">13.66</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.78</td>
    <td align="right">5.84</td>
    <td align="right">5.86</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.40</td>
    <td align="right">12.73</td>
    <td align="right">12.72</td>
    <td align="right">12.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.72</td>
    <td align="right">15.19</td>
    <td align="right">15.92</td>
    <td align="right">15.10</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.83</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.17</td>
    <td align="right">2.77</td>
    <td align="right">2.77</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.63</td>
    <td align="right">4.57</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.83</td>
    <td align="right">4.41</td>
    <td align="right">4.41</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.33</td>
    <td align="right">2.84</td>
    <td align="right">2.85</td>
    <td align="right">2.84</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.48</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.83</td>
    <td align="right">4.52</td>
    <td align="right">4.52</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.57</td>
    <td align="right">5.66</td>
    <td align="right">5.64</td>
    <td align="right">5.63</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.61</td>
    <td align="right">7.79</td>
    <td align="right">7.86</td>
    <td align="right">7.85</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.79</td>
    <td align="right">7.68</td>
    <td align="right">7.67</td>
    <td align="right">7.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.59</td>
    <td align="right">5.68</td>
    <td align="right">5.67</td>
    <td align="right">5.67</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.46</td>
    <td align="right">8.66</td>
    <td align="right">8.72</td>
    <td align="right">8.71</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.62</td>
    <td align="right">8.42</td>
    <td align="right">8.42</td>
    <td align="right">8.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.43</td>
    <td align="right">6.93</td>
    <td align="right">6.93</td>
    <td align="right">6.93</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.76</td>
    <td align="right">8.38</td>
    <td align="right">8.39</td>
    <td align="right">8.39</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.70</td>
    <td align="right">11.22</td>
    <td align="right">11.25</td>
    <td align="right">11.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.77</td>
    <td align="right">9.90</td>
    <td align="right">9.90</td>
    <td align="right">9.90</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">10.90</td>
    <td align="right">10.90</td>
    <td align="right">10.91</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.13</td>
    <td align="right">14.42</td>
    <td align="right">14.42</td>
    <td align="right">14.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.66</td>
    <td align="right">11.05</td>
    <td align="right">11.05</td>
    <td align="right">11.06</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.94</td>
    <td align="right">13.13</td>
    <td align="right">13.13</td>
    <td align="right">13.15</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.17</td>
    <td align="right">15.73</td>
    <td align="right">16.32</td>
    <td align="right">16.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.87</td>
    <td align="right">14.19</td>
    <td align="right">14.18</td>
    <td align="right">14.18</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.59</td>
    <td align="right">15.98</td>
    <td align="right">15.98</td>
    <td align="right">15.98</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.82</td>
    <td align="right">21.19</td>
    <td align="right">21.12</td>
    <td align="right">21.21</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.14</td>
    <td align="right">23.11</td>
    <td align="right">14.68</td>
    <td align="right">21.40</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">18.30</td>
    <td align="right">20.27</td>
    <td align="right">21.68</td>
    <td align="right">23.25</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.82</td>
    <td align="right">6.45</td>
    <td align="right">6.41</td>
    <td align="right">6.41</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.86</td>
    <td align="right">6.36</td>
    <td align="right">6.38</td>
    <td align="right">6.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.14</td>
    <td align="right">49.34</td>
    <td align="right">26.89</td>
    <td align="right">31.30</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.17</td>
    <td align="right">12.22</td>
    <td align="right">12.25</td>
    <td align="right">12.23</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.35</td>
    <td align="right">12.39</td>
    <td align="right">12.39</td>
    <td align="right">12.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.98</td>
    <td align="right">95.66</td>
    <td align="right">34.22</td>
    <td align="right">43.52</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.90</td>
    <td align="right">18.69</td>
    <td align="right">18.70</td>
    <td align="right">18.70</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.05</td>
    <td align="right">19.26</td>
    <td align="right">19.25</td>
    <td align="right">19.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.18</td>
    <td align="right">137.05</td>
    <td align="right">40.11</td>
    <td align="right">54.69</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.35</td>
    <td align="right">22.32</td>
    <td align="right">22.32</td>
    <td align="right">22.33</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.92</td>
    <td align="right">25.51</td>
    <td align="right">25.51</td>
    <td align="right">25.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.61</td>
    <td align="right">7.33</td>
    <td align="right">7.35</td>
    <td align="right">7.36</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.80</td>
    <td align="right">8.59</td>
    <td align="right">8.59</td>
    <td align="right">8.61</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.41</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.24</td>
    <td align="right">15.58</td>
    <td align="right">15.64</td>
    <td align="right">15.55</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.06</td>
    <td align="right">20.17</td>
    <td align="right">20.20</td>
    <td align="right">20.17</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.63</td>
    <td align="right">7.92</td>
    <td align="right">7.93</td>
    <td align="right">7.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">30.02</td>
    <td align="right">31.59</td>
    <td align="right">31.59</td>
    <td align="right">31.59</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.72</td>
    <td align="right">35.30</td>
    <td align="right">35.36</td>
    <td align="right">35.33</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.18</td>
    <td align="right">21.15</td>
    <td align="right">21.17</td>
    <td align="right">21.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.47</td>
    <td align="right">39.55</td>
    <td align="right">39.57</td>
    <td align="right">39.58</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">41.01</td>
    <td align="right">52.09</td>
    <td align="right">53.04</td>
    <td align="right">52.19</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.00</td>
    <td align="right">24.27</td>
    <td align="right">24.34</td>
    <td align="right">24.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.34</td>
    <td align="right">4.03</td>
    <td align="right">4.02</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.68</td>
    <td align="right">5.70</td>
    <td align="right">5.74</td>
    <td align="right">5.72</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.97</td>
    <td align="right">5.82</td>
    <td align="right">5.78</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.97</td>
    <td align="right">8.82</td>
    <td align="right">8.81</td>
    <td align="right">8.83</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.01</td>
    <td align="right">10.03</td>
    <td align="right">10.05</td>
    <td align="right">10.07</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.73</td>
    <td align="right">12.79</td>
    <td align="right">12.82</td>
    <td align="right">12.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.98</td>
    <td align="right">21.23</td>
    <td align="right">21.23</td>
    <td align="right">21.24</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.36</td>
    <td align="right">26.42</td>
    <td align="right">26.46</td>
    <td align="right">26.45</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.40</td>
    <td align="right">27.15</td>
    <td align="right">27.16</td>
    <td align="right">27.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.97</td>
    <td align="right">24.79</td>
    <td align="right">24.80</td>
    <td align="right">24.80</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.02</td>
    <td align="right">31.99</td>
    <td align="right">32.01</td>
    <td align="right">32.02</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">30.51</td>
    <td align="right">32.09</td>
    <td align="right">32.10</td>
    <td align="right">32.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.93</td>
    <td align="right">8.54</td>
    <td align="right">8.54</td>
    <td align="right">8.53</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.61</td>
    <td align="right">10.16</td>
    <td align="right">10.21</td>
    <td align="right">10.16</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.35</td>
    <td align="right">15.55</td>
    <td align="right">15.59</td>
    <td align="right">15.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.73</td>
    <td align="right">18.87</td>
    <td align="right">18.90</td>
    <td align="right">18.86</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">20.49</td>
    <td align="right">20.08</td>
    <td align="right">20.10</td>
    <td align="right">20.15</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.42</td>
    <td align="right">32.72</td>
    <td align="right">32.72</td>
    <td align="right">32.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.00</td>
    <td align="right">28.12</td>
    <td align="right">28.11</td>
    <td align="right">28.14</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.60</td>
    <td align="right">40.74</td>
    <td align="right">40.80</td>
    <td align="right">40.79</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">43.93</td>
    <td align="right">49.91</td>
    <td align="right">49.90</td>
    <td align="right">49.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.53</td>
    <td align="right">43.86</td>
    <td align="right">43.93</td>
    <td align="right">43.85</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.28</td>
    <td align="right">53.17</td>
    <td align="right">53.17</td>
    <td align="right">53.18</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.22</td>
    <td align="right">74.76</td>
    <td align="right">74.66</td>
    <td align="right">74.76</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.27</td>
    <td align="right">6.03</td>
    <td align="right">4.27</td>
    <td align="right">7.19</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.41</td>
    <td align="right">10.95</td>
    <td align="right">17.46</td>
    <td align="right">18.65</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.05</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.67</td>
    <td align="right">16.08</td>
    <td align="right">18.57</td>
    <td align="right">21.43</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">4.69</td>
    <td align="right">4.68</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.87</td>
    <td align="right">19.78</td>
    <td align="right">17.56</td>
    <td align="right">21.07</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.92</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.68</td>
    <td align="right">24.08</td>
    <td align="right">18.27</td>
    <td align="right">22.72</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">5.74</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.32</td>
    <td align="right">3.46</td>
    <td align="right">3.46</td>
    <td align="right">3.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.24</td>
    <td align="right">3.86</td>
    <td align="right">3.87</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.35</td>
    <td align="right">3.70</td>
    <td align="right">3.69</td>
    <td align="right">3.71</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.37</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.05</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.84</td>
    <td align="right">7.77</td>
    <td align="right">7.75</td>
    <td align="right">7.75</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.96</td>
    <td align="right">7.43</td>
    <td align="right">7.42</td>
    <td align="right">7.42</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.39</td>
    <td align="right">4.46</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.16</td>
    <td align="right">8.17</td>
    <td align="right">8.17</td>
    <td align="right">8.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.95</td>
    <td align="right">8.34</td>
    <td align="right">8.33</td>
    <td align="right">8.34</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.44</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.86</td>
    <td align="right">2.48</td>
    <td align="right">2.49</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.90</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.09</td>
    <td align="right">4.02</td>
    <td align="right">4.00</td>
    <td align="right">4.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.96</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">3.88</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.24</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.44</td>
    <td align="right">4.20</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.80</td>
    <td align="right">6.41</td>
    <td align="right">6.42</td>
    <td align="right">6.42</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.03</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.50</td>
    <td align="right">4.22</td>
    <td align="right">4.21</td>
    <td align="right">4.22</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.92</td>
    <td align="right">7.37</td>
    <td align="right">7.39</td>
    <td align="right">7.36</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.23</td>
    <td align="right">7.16</td>
    <td align="right">7.13</td>
    <td align="right">7.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.32</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.73</td>
    <td align="right">8.04</td>
    <td align="right">8.04</td>
    <td align="right">8.03</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.34</td>
    <td align="right">10.39</td>
    <td align="right">10.41</td>
    <td align="right">10.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.67</td>
    <td align="right">9.03</td>
    <td align="right">9.03</td>
    <td align="right">9.04</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.58</td>
    <td align="right">10.28</td>
    <td align="right">10.28</td>
    <td align="right">10.27</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.97</td>
    <td align="right">14.54</td>
    <td align="right">14.60</td>
    <td align="right">14.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.96</td>
    <td align="right">10.85</td>
    <td align="right">10.86</td>
    <td align="right">10.86</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.34</td>
    <td align="right">12.44</td>
    <td align="right">12.43</td>
    <td align="right">12.43</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.77</td>
    <td align="right">15.81</td>
    <td align="right">15.86</td>
    <td align="right">15.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.29</td>
    <td align="right">13.72</td>
    <td align="right">13.72</td>
    <td align="right">13.72</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.18</td>
    <td align="right">15.41</td>
    <td align="right">15.39</td>
    <td align="right">15.39</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.76</td>
    <td align="right">20.99</td>
    <td align="right">21.28</td>
    <td align="right">20.93</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.10</td>
    <td align="right">23.41</td>
    <td align="right">14.52</td>
    <td align="right">21.27</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.29</td>
    <td align="right">13.82</td>
    <td align="right">20.07</td>
    <td align="right">21.49</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.15</td>
    <td align="right">6.16</td>
    <td align="right">6.20</td>
    <td align="right">6.19</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.19</td>
    <td align="right">6.80</td>
    <td align="right">6.77</td>
    <td align="right">6.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.51</td>
    <td align="right">50.41</td>
    <td align="right">26.44</td>
    <td align="right">31.03</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.35</td>
    <td align="right">11.31</td>
    <td align="right">11.34</td>
    <td align="right">11.35</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.24</td>
    <td align="right">12.28</td>
    <td align="right">12.29</td>
    <td align="right">12.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.85</td>
    <td align="right">87.25</td>
    <td align="right">31.72</td>
    <td align="right">39.99</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.05</td>
    <td align="right">18.19</td>
    <td align="right">18.19</td>
    <td align="right">18.20</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.57</td>
    <td align="right">19.58</td>
    <td align="right">19.61</td>
    <td align="right">19.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.88</td>
    <td align="right">121.66</td>
    <td align="right">37.42</td>
    <td align="right">50.57</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.36</td>
    <td align="right">22.19</td>
    <td align="right">22.22</td>
    <td align="right">22.21</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">13.98</td>
    <td align="right">15.26</td>
    <td align="right">15.26</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.76</td>
    <td align="right">5.63</td>
    <td align="right">5.62</td>
    <td align="right">5.64</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.46</td>
    <td align="right">5.09</td>
    <td align="right">5.12</td>
    <td align="right">5.11</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.14</td>
    <td align="right">3.98</td>
    <td align="right">3.97</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.67</td>
    <td align="right">10.45</td>
    <td align="right">10.46</td>
    <td align="right">10.43</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.60</td>
    <td align="right">12.26</td>
    <td align="right">12.27</td>
    <td align="right">12.25</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.90</td>
    <td align="right">7.61</td>
    <td align="right">7.60</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">18.26</td>
    <td align="right">22.27</td>
    <td align="right">22.26</td>
    <td align="right">22.26</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.29</td>
    <td align="right">23.15</td>
    <td align="right">23.15</td>
    <td align="right">23.16</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.31</td>
    <td align="right">16.71</td>
    <td align="right">16.70</td>
    <td align="right">16.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.52</td>
    <td align="right">30.03</td>
    <td align="right">30.04</td>
    <td align="right">30.03</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.17</td>
    <td align="right">30.82</td>
    <td align="right">30.78</td>
    <td align="right">30.81</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.94</td>
    <td align="right">18.57</td>
    <td align="right">18.57</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.97</td>
    <td align="right">3.75</td>
    <td align="right">3.74</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.20</td>
    <td align="right">5.68</td>
    <td align="right">5.69</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.88</td>
    <td align="right">4.82</td>
    <td align="right">4.78</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.30</td>
    <td align="right">7.34</td>
    <td align="right">7.33</td>
    <td align="right">7.34</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.47</td>
    <td align="right">10.13</td>
    <td align="right">10.13</td>
    <td align="right">10.11</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.94</td>
    <td align="right">12.44</td>
    <td align="right">12.41</td>
    <td align="right">12.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.37</td>
    <td align="right">16.36</td>
    <td align="right">16.38</td>
    <td align="right">16.37</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.11</td>
    <td align="right">21.69</td>
    <td align="right">21.73</td>
    <td align="right">21.71</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.32</td>
    <td align="right">21.99</td>
    <td align="right">21.97</td>
    <td align="right">21.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.27</td>
    <td align="right">18.57</td>
    <td align="right">18.55</td>
    <td align="right">18.57</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.43</td>
    <td align="right">30.35</td>
    <td align="right">30.42</td>
    <td align="right">30.37</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">24.98</td>
    <td align="right">29.68</td>
    <td align="right">29.72</td>
    <td align="right">29.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.27</td>
    <td align="right">8.72</td>
    <td align="right">8.66</td>
    <td align="right">8.70</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.06</td>
    <td align="right">10.53</td>
    <td align="right">10.54</td>
    <td align="right">10.57</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">12.77</td>
    <td align="right">12.66</td>
    <td align="right">12.71</td>
    <td align="right">12.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.00</td>
    <td align="right">18.17</td>
    <td align="right">18.14</td>
    <td align="right">18.18</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.86</td>
    <td align="right">22.26</td>
    <td align="right">22.20</td>
    <td align="right">22.20</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.11</td>
    <td align="right">31.51</td>
    <td align="right">31.59</td>
    <td align="right">31.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.62</td>
    <td align="right">31.75</td>
    <td align="right">31.73</td>
    <td align="right">31.88</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">37.63</td>
    <td align="right">40.62</td>
    <td align="right">40.59</td>
    <td align="right">40.52</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">44.55</td>
    <td align="right">48.83</td>
    <td align="right">48.99</td>
    <td align="right">49.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">44.38</td>
    <td align="right">43.58</td>
    <td align="right">43.61</td>
    <td align="right">43.56</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">53.75</td>
    <td align="right">52.41</td>
    <td align="right">52.08</td>
    <td align="right">52.38</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.92</td>
    <td align="right">71.38</td>
    <td align="right">70.59</td>
    <td align="right">70.88</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.75</td>
    <td align="right">2.71</td>
    <td align="right">1.97</td>
    <td align="right">4.22</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.35</td>
    <td align="right">4.13</td>
    <td align="right">11.37</td>
    <td align="right">11.75</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.45</td>
    <td align="right">6.09</td>
    <td align="right">11.96</td>
    <td align="right">12.81</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.69</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.61</td>
    <td align="right">7.34</td>
    <td align="right">11.22</td>
    <td align="right">12.77</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">15.03</td>
    <td align="right">9.35</td>
    <td align="right">11.41</td>
    <td align="right">13.43</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.79</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.24</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
    <td align="right">1.72</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.25</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.99</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">2.18</td>
    <td align="right">2.22</td>
    <td align="right">2.17</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.39</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.03</td>
    <td align="right">2.89</td>
    <td align="right">2.89</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.03</td>
    <td align="right">3.00</td>
    <td align="right">2.99</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.89</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="right">2.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.61</td>
    <td align="right">3.34</td>
    <td align="right">3.33</td>
    <td align="right">3.33</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.64</td>
    <td align="right">3.59</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.93</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="right">2.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.02</td>
    <td align="right">1.71</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.24</td>
    <td align="right">1.74</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.30</td>
    <td align="right">1.75</td>
    <td align="right">1.77</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.04</td>
    <td align="right">1.59</td>
    <td align="right">1.60</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.73</td>
    <td align="right">2.16</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.97</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.11</td>
    <td align="right">2.91</td>
    <td align="right">2.94</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.07</td>
    <td align="right">3.07</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.92</td>
    <td align="right">2.83</td>
    <td align="right">2.83</td>
    <td align="right">2.82</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.51</td>
    <td align="right">3.34</td>
    <td align="right">3.37</td>
    <td align="right">3.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.66</td>
    <td align="right">3.58</td>
    <td align="right">3.58</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.21</td>
    <td align="right">2.85</td>
    <td align="right">2.88</td>
    <td align="right">2.87</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.99</td>
    <td align="right">3.85</td>
    <td align="right">3.92</td>
    <td align="right">3.85</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.72</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.82</td>
    <td align="right">3.85</td>
    <td align="right">3.84</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.40</td>
    <td align="right">4.26</td>
    <td align="right">4.28</td>
    <td align="right">4.27</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.89</td>
    <td align="right">6.83</td>
    <td align="right">6.82</td>
    <td align="right">6.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.53</td>
    <td align="right">4.58</td>
    <td align="right">4.57</td>
    <td align="right">4.56</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.47</td>
    <td align="right">5.24</td>
    <td align="right">5.24</td>
    <td align="right">5.26</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.05</td>
    <td align="right">7.59</td>
    <td align="right">7.58</td>
    <td align="right">7.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">5.78</td>
    <td align="right">5.79</td>
    <td align="right">5.78</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.40</td>
    <td align="right">6.06</td>
    <td align="right">6.05</td>
    <td align="right">6.05</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.12</td>
    <td align="right">10.62</td>
    <td align="right">10.61</td>
    <td align="right">10.62</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.50</td>
    <td align="right">11.15</td>
    <td align="right">6.35</td>
    <td align="right">9.58</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.81</td>
    <td align="right">6.16</td>
    <td align="right">12.92</td>
    <td align="right">13.40</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.05</td>
    <td align="right">1.98</td>
    <td align="right">1.99</td>
    <td align="right">2.00</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.11</td>
    <td align="right">2.02</td>
    <td align="right">2.02</td>
    <td align="right">2.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">12.93</td>
    <td align="right">11.19</td>
    <td align="right">16.12</td>
    <td align="right">17.85</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.72</td>
    <td align="right">3.51</td>
    <td align="right">3.62</td>
    <td align="right">3.82</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.28</td>
    <td align="right">3.11</td>
    <td align="right">3.16</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.49</td>
    <td align="right">25.11</td>
    <td align="right">18.31</td>
    <td align="right">22.21</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.99</td>
    <td align="right">6.55</td>
    <td align="right">6.69</td>
    <td align="right">6.49</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.49</td>
    <td align="right">6.30</td>
    <td align="right">5.92</td>
    <td align="right">6.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.51</td>
    <td align="right">39.20</td>
    <td align="right">20.66</td>
    <td align="right">27.58</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.94</td>
    <td align="right">8.08</td>
    <td align="right">7.92</td>
    <td align="right">7.92</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">8.16</td>
    <td align="right">6.45</td>
    <td align="right">6.32</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.73</td>
    <td align="right">2.63</td>
    <td align="right">2.61</td>
    <td align="right">2.62</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.41</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.10</td>
    <td align="right">4.15</td>
    <td align="right">4.20</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.22</td>
    <td align="right">4.57</td>
    <td align="right">4.46</td>
    <td align="right">4.48</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.66</td>
    <td align="right">3.28</td>
    <td align="right">3.24</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.04</td>
    <td align="right">9.14</td>
    <td align="right">9.35</td>
    <td align="right">9.95</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.80</td>
    <td align="right">9.67</td>
    <td align="right">9.80</td>
    <td align="right">10.01</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.20</td>
    <td align="right">8.50</td>
    <td align="right">8.14</td>
    <td align="right">7.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.51</td>
    <td align="right">12.72</td>
    <td align="right">13.20</td>
    <td align="right">13.02</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">16.24</td>
    <td align="right">13.64</td>
    <td align="right">13.59</td>
    <td align="right">13.70</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.43</td>
    <td align="right">11.55</td>
    <td align="right">11.15</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.41</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.71</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.98</td>
    <td align="right">3.31</td>
    <td align="right">3.25</td>
    <td align="right">3.22</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.94</td>
    <td align="right">4.25</td>
    <td align="right">4.24</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.19</td>
    <td align="right">5.06</td>
    <td align="right">4.46</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">8.08</td>
    <td align="right">8.55</td>
    <td align="right">8.13</td>
    <td align="right">7.55</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.59</td>
    <td align="right">8.87</td>
    <td align="right">9.37</td>
    <td align="right">9.49</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.00</td>
    <td align="right">9.81</td>
    <td align="right">10.02</td>
    <td align="right">9.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">10.27</td>
    <td align="right">11.21</td>
    <td align="right">11.53</td>
    <td align="right">11.18</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.90</td>
    <td align="right">12.88</td>
    <td align="right">12.91</td>
    <td align="right">12.90</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.78</td>
    <td align="right">13.12</td>
    <td align="right">13.32</td>
    <td align="right">13.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.59</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="right">4.25</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.75</td>
    <td align="right">5.12</td>
    <td align="right">5.14</td>
    <td align="right">5.10</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.96</td>
    <td align="right">6.76</td>
    <td align="right">6.76</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">9.54</td>
    <td align="right">8.55</td>
    <td align="right">8.87</td>
    <td align="right">8.29</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.22</td>
    <td align="right">8.47</td>
    <td align="right">8.48</td>
    <td align="right">7.94</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.11</td>
    <td align="right">12.65</td>
    <td align="right">12.29</td>
    <td align="right">12.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">16.40</td>
    <td align="right">14.83</td>
    <td align="right">14.78</td>
    <td align="right">14.96</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">23.92</td>
    <td align="right">16.91</td>
    <td align="right">17.58</td>
    <td align="right">17.08</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">26.57</td>
    <td align="right">23.06</td>
    <td align="right">23.20</td>
    <td align="right">23.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">23.85</td>
    <td align="right">19.24</td>
    <td align="right">18.56</td>
    <td align="right">17.80</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.15</td>
    <td align="right">20.59</td>
    <td align="right">20.57</td>
    <td align="right">20.59</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.61</td>
    <td align="right">35.47</td>
    <td align="right">35.47</td>
    <td align="right">35.47</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.13</td>
    <td align="right">5.19</td>
    <td align="right">3.53</td>
    <td align="right">5.49</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.31</td>
    <td align="right">11.32</td>
    <td align="right">14.07</td>
    <td align="right">15.20</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.57</td>
    <td align="right">3.57</td>
    <td align="right">3.56</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.34</td>
    <td align="right">4.16</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.12</td>
    <td align="right">15.92</td>
    <td align="right">14.72</td>
    <td align="right">16.25</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.40</td>
    <td align="right">3.99</td>
    <td align="right">3.99</td>
    <td align="right">3.94</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.80</td>
    <td align="right">4.77</td>
    <td align="right">4.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.22</td>
    <td align="right">20.28</td>
    <td align="right">13.99</td>
    <td align="right">16.95</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.04</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="right">4.35</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.68</td>
    <td align="right">5.18</td>
    <td align="right">5.15</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.81</td>
    <td align="right">25.11</td>
    <td align="right">14.30</td>
    <td align="right">17.72</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.71</td>
    <td align="right">4.71</td>
    <td align="right">4.70</td>
    <td align="right">4.68</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.30</td>
    <td align="right">5.63</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.37</td>
    <td align="right">4.29</td>
    <td align="right">4.28</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.39</td>
    <td align="right">4.62</td>
    <td align="right">4.60</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.84</td>
    <td align="right">2.18</td>
    <td align="right">2.17</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.22</td>
    <td align="right">7.00</td>
    <td align="right">6.81</td>
    <td align="right">6.82</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.71</td>
    <td align="right">7.06</td>
    <td align="right">7.04</td>
    <td align="right">7.02</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.82</td>
    <td align="right">2.16</td>
    <td align="right">2.15</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.51</td>
    <td align="right">9.21</td>
    <td align="right">9.02</td>
    <td align="right">9.03</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.34</td>
    <td align="right">10.50</td>
    <td align="right">10.24</td>
    <td align="right">10.25</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.28</td>
    <td align="right">3.50</td>
    <td align="right">3.49</td>
    <td align="right">3.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.61</td>
    <td align="right">10.19</td>
    <td align="right">10.20</td>
    <td align="right">10.22</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.86</td>
    <td align="right">12.35</td>
    <td align="right">12.18</td>
    <td align="right">12.15</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.31</td>
    <td align="right">3.49</td>
    <td align="right">3.47</td>
    <td align="right">3.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.80</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.03</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.73</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.79</td>
    <td align="right">3.14</td>
    <td align="right">3.13</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">2.08</td>
    <td align="right">2.05</td>
    <td align="right">2.03</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.15</td>
    <td align="right">4.41</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.65</td>
    <td align="right">5.19</td>
    <td align="right">5.15</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.35</td>
    <td align="right">3.31</td>
    <td align="right">3.23</td>
    <td align="right">3.24</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.89</td>
    <td align="right">6.63</td>
    <td align="right">6.60</td>
    <td align="right">6.59</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.68</td>
    <td align="right">6.43</td>
    <td align="right">6.39</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.44</td>
    <td align="right">3.33</td>
    <td align="right">3.32</td>
    <td align="right">3.31</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.85</td>
    <td align="right">7.64</td>
    <td align="right">7.61</td>
    <td align="right">7.53</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.07</td>
    <td align="right">7.17</td>
    <td align="right">7.17</td>
    <td align="right">7.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.02</td>
    <td align="right">6.00</td>
    <td align="right">6.01</td>
    <td align="right">6.02</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">9.94</td>
    <td align="right">7.41</td>
    <td align="right">7.39</td>
    <td align="right">7.44</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.07</td>
    <td align="right">8.90</td>
    <td align="right">8.96</td>
    <td align="right">8.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.39</td>
    <td align="right">8.09</td>
    <td align="right">8.07</td>
    <td align="right">7.92</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.68</td>
    <td align="right">9.12</td>
    <td align="right">9.03</td>
    <td align="right">8.96</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.73</td>
    <td align="right">12.97</td>
    <td align="right">12.98</td>
    <td align="right">12.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.37</td>
    <td align="right">10.67</td>
    <td align="right">10.65</td>
    <td align="right">10.61</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.14</td>
    <td align="right">12.68</td>
    <td align="right">12.63</td>
    <td align="right">12.45</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.42</td>
    <td align="right">15.32</td>
    <td align="right">15.31</td>
    <td align="right">15.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.69</td>
    <td align="right">12.64</td>
    <td align="right">12.64</td>
    <td align="right">12.60</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.31</td>
    <td align="right">14.19</td>
    <td align="right">14.18</td>
    <td align="right">14.08</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.51</td>
    <td align="right">22.81</td>
    <td align="right">22.64</td>
    <td align="right">22.52</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">39.87</td>
    <td align="right">23.30</td>
    <td align="right">12.15</td>
    <td align="right">18.53</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.00</td>
    <td align="right">11.78</td>
    <td align="right">15.52</td>
    <td align="right">16.53</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.23</td>
    <td align="right">3.76</td>
    <td align="right">3.76</td>
    <td align="right">3.77</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.73</td>
    <td align="right">4.52</td>
    <td align="right">4.50</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">17.36</td>
    <td align="right">17.68</td>
    <td align="right">16.70</td>
    <td align="right">18.36</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.03</td>
    <td align="right">5.65</td>
    <td align="right">5.65</td>
    <td align="right">5.58</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.85</td>
    <td align="right">6.47</td>
    <td align="right">6.51</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.61</td>
    <td align="right">79.88</td>
    <td align="right">26.06</td>
    <td align="right">33.66</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.51</td>
    <td align="right">13.61</td>
    <td align="right">13.60</td>
    <td align="right">13.63</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.50</td>
    <td align="right">16.03</td>
    <td align="right">15.96</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.93</td>
    <td align="right">118.19</td>
    <td align="right">31.16</td>
    <td align="right">42.67</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.72</td>
    <td align="right">18.36</td>
    <td align="right">18.31</td>
    <td align="right">18.31</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.85</td>
    <td align="right">22.63</td>
    <td align="right">22.59</td>
    <td align="right">22.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.10</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.68</td>
    <td align="right">4.96</td>
    <td align="right">4.97</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.17</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.25</td>
    <td align="right">8.93</td>
    <td align="right">8.71</td>
    <td align="right">8.71</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.69</td>
    <td align="right">9.06</td>
    <td align="right">9.09</td>
    <td align="right">8.95</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.83</td>
    <td align="right">4.22</td>
    <td align="right">4.18</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.33</td>
    <td align="right">23.63</td>
    <td align="right">23.60</td>
    <td align="right">23.47</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.97</td>
    <td align="right">28.49</td>
    <td align="right">28.43</td>
    <td align="right">28.45</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.15</td>
    <td align="right">13.21</td>
    <td align="right">13.20</td>
    <td align="right">13.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.25</td>
    <td align="right">35.14</td>
    <td align="right">35.19</td>
    <td align="right">35.35</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.08</td>
    <td align="right">38.33</td>
    <td align="right">38.25</td>
    <td align="right">38.20</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.39</td>
    <td align="right">15.12</td>
    <td align="right">15.10</td>
    <td align="right">15.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.15</td>
    <td align="right">2.14</td>
    <td align="right">2.14</td>
    <td align="right">2.14</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.12</td>
    <td align="right">3.42</td>
    <td align="right">3.42</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.20</td>
    <td align="right">3.31</td>
    <td align="right">3.30</td>
    <td align="right">3.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.00</td>
    <td align="right">3.96</td>
    <td align="right">3.87</td>
    <td align="right">3.92</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.93</td>
    <td align="right">5.81</td>
    <td align="right">5.90</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.34</td>
    <td align="right">7.17</td>
    <td align="right">7.38</td>
    <td align="right">7.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.40</td>
    <td align="right">13.08</td>
    <td align="right">13.03</td>
    <td align="right">13.03</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.22</td>
    <td align="right">19.34</td>
    <td align="right">19.32</td>
    <td align="right">19.31</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.97</td>
    <td align="right">19.29</td>
    <td align="right">19.29</td>
    <td align="right">19.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.86</td>
    <td align="right">15.06</td>
    <td align="right">15.03</td>
    <td align="right">15.03</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.83</td>
    <td align="right">27.81</td>
    <td align="right">27.81</td>
    <td align="right">27.75</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.94</td>
    <td align="right">27.64</td>
    <td align="right">27.55</td>
    <td align="right">27.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.66</td>
    <td align="right">6.43</td>
    <td align="right">6.41</td>
    <td align="right">6.41</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.57</td>
    <td align="right">7.97</td>
    <td align="right">7.97</td>
    <td align="right">7.96</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.43</td>
    <td align="right">9.95</td>
    <td align="right">9.91</td>
    <td align="right">9.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.20</td>
    <td align="right">9.72</td>
    <td align="right">9.57</td>
    <td align="right">9.64</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.08</td>
    <td align="right">11.05</td>
    <td align="right">11.43</td>
    <td align="right">11.28</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.54</td>
    <td align="right">14.04</td>
    <td align="right">14.04</td>
    <td align="right">14.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.60</td>
    <td align="right">24.12</td>
    <td align="right">24.09</td>
    <td align="right">24.01</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.63</td>
    <td align="right">32.26</td>
    <td align="right">32.32</td>
    <td align="right">32.33</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.35</td>
    <td align="right">40.11</td>
    <td align="right">40.16</td>
    <td align="right">40.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.74</td>
    <td align="right">33.50</td>
    <td align="right">33.42</td>
    <td align="right">33.64</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.92</td>
    <td align="right">40.83</td>
    <td align="right">40.70</td>
    <td align="right">40.79</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.03</td>
    <td align="right">64.87</td>
    <td align="right">64.85</td>
    <td align="right">64.75</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.48</td>
    <td align="right">34.12</td>
    <td align="right">14.23</td>
    <td align="right">17.71</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">31.06</td>
    <td align="right">44.58</td>
    <td align="right">39.39</td>
    <td align="right">40.81</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.31</td>
    <td align="right">16.23</td>
    <td align="right">16.20</td>
    <td align="right">16.20</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.57</td>
    <td align="right">17.55</td>
    <td align="right">17.67</td>
    <td align="right">17.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.61</td>
    <td align="right">67.00</td>
    <td align="right">40.59</td>
    <td align="right">45.22</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.36</td>
    <td align="right">18.59</td>
    <td align="right">18.46</td>
    <td align="right">18.48</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">19.44</td>
    <td align="right">19.07</td>
    <td align="right">19.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.25</td>
    <td align="right">81.92</td>
    <td align="right">38.88</td>
    <td align="right">46.16</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.38</td>
    <td align="right">20.52</td>
    <td align="right">20.47</td>
    <td align="right">20.47</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.00</td>
    <td align="right">21.29</td>
    <td align="right">20.98</td>
    <td align="right">21.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.77</td>
    <td align="right">103.54</td>
    <td align="right">41.16</td>
    <td align="right">49.31</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.64</td>
    <td align="right">22.16</td>
    <td align="right">22.15</td>
    <td align="right">22.17</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.36</td>
    <td align="right">22.04</td>
    <td align="right">22.10</td>
    <td align="right">22.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.92</td>
    <td align="right">23.82</td>
    <td align="right">23.80</td>
    <td align="right">23.77</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.27</td>
    <td align="right">26.52</td>
    <td align="right">26.51</td>
    <td align="right">26.52</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.87</td>
    <td align="right">15.53</td>
    <td align="right">15.67</td>
    <td align="right">15.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.65</td>
    <td align="right">30.02</td>
    <td align="right">30.24</td>
    <td align="right">29.97</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.00</td>
    <td align="right">34.55</td>
    <td align="right">34.55</td>
    <td align="right">34.57</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.96</td>
    <td align="right">18.13</td>
    <td align="right">18.38</td>
    <td align="right">17.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.52</td>
    <td align="right">36.92</td>
    <td align="right">37.02</td>
    <td align="right">36.93</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.50</td>
    <td align="right">49.05</td>
    <td align="right">48.97</td>
    <td align="right">48.96</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.24</td>
    <td align="right">20.82</td>
    <td align="right">20.82</td>
    <td align="right">20.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.39</td>
    <td align="right">41.70</td>
    <td align="right">41.65</td>
    <td align="right">41.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.51</td>
    <td align="right">58.61</td>
    <td align="right">58.56</td>
    <td align="right">58.60</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.96</td>
    <td align="right">26.06</td>
    <td align="right">26.00</td>
    <td align="right">26.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.42</td>
    <td align="right">16.83</td>
    <td align="right">16.83</td>
    <td align="right">16.87</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.91</td>
    <td align="right">23.70</td>
    <td align="right">23.71</td>
    <td align="right">23.76</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.54</td>
    <td align="right">26.54</td>
    <td align="right">26.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.03</td>
    <td align="right">21.04</td>
    <td align="right">21.29</td>
    <td align="right">21.08</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.64</td>
    <td align="right">30.17</td>
    <td align="right">30.18</td>
    <td align="right">29.97</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.01</td>
    <td align="right">34.55</td>
    <td align="right">34.54</td>
    <td align="right">34.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.43</td>
    <td align="right">25.07</td>
    <td align="right">25.06</td>
    <td align="right">25.15</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.44</td>
    <td align="right">36.91</td>
    <td align="right">37.01</td>
    <td align="right">36.94</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.68</td>
    <td align="right">49.09</td>
    <td align="right">48.97</td>
    <td align="right">48.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.64</td>
    <td align="right">33.06</td>
    <td align="right">33.06</td>
    <td align="right">33.32</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.39</td>
    <td align="right">41.58</td>
    <td align="right">41.67</td>
    <td align="right">41.52</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.38</td>
    <td align="right">58.54</td>
    <td align="right">58.53</td>
    <td align="right">58.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.32</td>
    <td align="right">24.19</td>
    <td align="right">24.42</td>
    <td align="right">24.38</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.64</td>
    <td align="right">32.51</td>
    <td align="right">32.51</td>
    <td align="right">32.56</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.86</td>
    <td align="right">34.56</td>
    <td align="right">34.37</td>
    <td align="right">34.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.42</td>
    <td align="right">33.63</td>
    <td align="right">33.64</td>
    <td align="right">33.66</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">44.91</td>
    <td align="right">39.32</td>
    <td align="right">39.34</td>
    <td align="right">39.33</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.69</td>
    <td align="right">44.74</td>
    <td align="right">44.72</td>
    <td align="right">44.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.08</td>
    <td align="right">41.18</td>
    <td align="right">41.10</td>
    <td align="right">41.09</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.44</td>
    <td align="right">48.15</td>
    <td align="right">48.17</td>
    <td align="right">48.17</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.29</td>
    <td align="right">47.37</td>
    <td align="right">47.44</td>
    <td align="right">47.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.25</td>
    <td align="right">46.80</td>
    <td align="right">46.74</td>
    <td align="right">46.87</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.31</td>
    <td align="right">52.43</td>
    <td align="right">52.38</td>
    <td align="right">52.40</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.13</td>
    <td align="right">64.46</td>
    <td align="right">64.93</td>
    <td align="right">65.76</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">109.11</td>
    <td align="right">128.91</td>
    <td align="right">28.15</td>
    <td align="right">41.68</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">39.51</td>
    <td align="right">56.07</td>
    <td align="right">46.54</td>
    <td align="right">47.16</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.18</td>
    <td align="right">18.02</td>
    <td align="right">18.06</td>
    <td align="right">18.11</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.00</td>
    <td align="right">19.84</td>
    <td align="right">20.35</td>
    <td align="right">19.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">100.93</td>
    <td align="right">129.53</td>
    <td align="right">61.35</td>
    <td align="right">68.46</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.86</td>
    <td align="right">26.78</td>
    <td align="right">26.53</td>
    <td align="right">26.76</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.86</td>
    <td align="right">33.24</td>
    <td align="right">33.20</td>
    <td align="right">33.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">190.97</td>
    <td align="right">255.35</td>
    <td align="right">79.53</td>
    <td align="right">99.13</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.10</td>
    <td align="right">48.02</td>
    <td align="right">48.00</td>
    <td align="right">47.98</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.26</td>
    <td align="right">50.31</td>
    <td align="right">50.28</td>
    <td align="right">50.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">299.48</td>
    <td align="right">411.67</td>
    <td align="right">106.73</td>
    <td align="right">140.12</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">48.47</td>
    <td align="right">66.06</td>
    <td align="right">65.94</td>
    <td align="right">66.05</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">63.33</td>
    <td align="right">66.81</td>
    <td align="right">66.77</td>
    <td align="right">66.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.63</td>
    <td align="right">27.07</td>
    <td align="right">26.99</td>
    <td align="right">27.00</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.83</td>
    <td align="right">32.35</td>
    <td align="right">32.42</td>
    <td align="right">32.40</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.04</td>
    <td align="right">18.54</td>
    <td align="right">18.11</td>
    <td align="right">18.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.84</td>
    <td align="right">44.29</td>
    <td align="right">44.29</td>
    <td align="right">44.24</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.82</td>
    <td align="right">52.47</td>
    <td align="right">52.57</td>
    <td align="right">52.48</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.49</td>
    <td align="right">27.98</td>
    <td align="right">27.38</td>
    <td align="right">28.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.88</td>
    <td align="right">71.54</td>
    <td align="right">71.58</td>
    <td align="right">71.60</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.37</td>
    <td align="right">82.91</td>
    <td align="right">82.92</td>
    <td align="right">82.89</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">43.23</td>
    <td align="right">45.59</td>
    <td align="right">45.62</td>
    <td align="right">45.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.68</td>
    <td align="right">97.39</td>
    <td align="right">99.42</td>
    <td align="right">98.56</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.23</td>
    <td align="right">112.08</td>
    <td align="right">112.19</td>
    <td align="right">112.18</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">71.84</td>
    <td align="right">77.85</td>
    <td align="right">77.75</td>
    <td align="right">77.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.46</td>
    <td align="right">20.47</td>
    <td align="right">19.97</td>
    <td align="right">21.13</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.00</td>
    <td align="right">28.02</td>
    <td align="right">27.93</td>
    <td align="right">27.91</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.12</td>
    <td align="right">31.60</td>
    <td align="right">31.67</td>
    <td align="right">31.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">31.61</td>
    <td align="right">33.43</td>
    <td align="right">33.41</td>
    <td align="right">33.82</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.33</td>
    <td align="right">42.17</td>
    <td align="right">42.12</td>
    <td align="right">42.11</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">56.89</td>
    <td align="right">54.73</td>
    <td align="right">54.70</td>
    <td align="right">54.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">49.31</td>
    <td align="right">57.34</td>
    <td align="right">57.30</td>
    <td align="right">58.44</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.15</td>
    <td align="right">73.58</td>
    <td align="right">73.67</td>
    <td align="right">73.39</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.93</td>
    <td align="right">83.13</td>
    <td align="right">85.17</td>
    <td align="right">84.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">84.38</td>
    <td align="right">85.42</td>
    <td align="right">85.13</td>
    <td align="right">85.08</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.57</td>
    <td align="right">97.22</td>
    <td align="right">96.98</td>
    <td align="right">96.93</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.75</td>
    <td align="right">112.07</td>
    <td align="right">112.12</td>
    <td align="right">112.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.50</td>
    <td align="right">27.60</td>
    <td align="right">27.47</td>
    <td align="right">27.45</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.77</td>
    <td align="right">38.68</td>
    <td align="right">38.77</td>
    <td align="right">40.37</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">37.72</td>
    <td align="right">40.95</td>
    <td align="right">41.06</td>
    <td align="right">41.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">43.12</td>
    <td align="right">44.77</td>
    <td align="right">44.77</td>
    <td align="right">44.82</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.13</td>
    <td align="right">59.74</td>
    <td align="right">59.62</td>
    <td align="right">59.61</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">64.59</td>
    <td align="right">67.14</td>
    <td align="right">67.24</td>
    <td align="right">67.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">67.22</td>
    <td align="right">69.87</td>
    <td align="right">71.86</td>
    <td align="right">71.53</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.00</td>
    <td align="right">87.01</td>
    <td align="right">86.79</td>
    <td align="right">86.91</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.63</td>
    <td align="right">95.88</td>
    <td align="right">95.87</td>
    <td align="right">95.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">85.13</td>
    <td align="right">89.71</td>
    <td align="right">89.99</td>
    <td align="right">89.37</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">106.77</td>
    <td align="right">107.36</td>
    <td align="right">107.43</td>
    <td align="right">107.48</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">135.47</td>
    <td align="right">143.71</td>
    <td align="right">143.78</td>
    <td align="right">143.83</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.35</td>
    <td align="right">14.40</td>
    <td align="right">8.59</td>
    <td align="right">11.59</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.45</td>
    <td align="right">28.24</td>
    <td align="right">29.23</td>
    <td align="right">30.09</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">13.93</td>
    <td align="right">14.08</td>
    <td align="right">13.92</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.84</td>
    <td align="right">17.98</td>
    <td align="right">18.06</td>
    <td align="right">17.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.62</td>
    <td align="right">42.61</td>
    <td align="right">31.41</td>
    <td align="right">33.94</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.13</td>
    <td align="right">18.45</td>
    <td align="right">18.45</td>
    <td align="right">18.44</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.23</td>
    <td align="right">20.85</td>
    <td align="right">20.86</td>
    <td align="right">20.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.38</td>
    <td align="right">62.86</td>
    <td align="right">32.19</td>
    <td align="right">39.38</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.58</td>
    <td align="right">21.32</td>
    <td align="right">21.31</td>
    <td align="right">21.32</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.12</td>
    <td align="right">22.90</td>
    <td align="right">22.82</td>
    <td align="right">22.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">59.42</td>
    <td align="right">81.79</td>
    <td align="right">32.84</td>
    <td align="right">39.36</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.24</td>
    <td align="right">23.26</td>
    <td align="right">23.26</td>
    <td align="right">23.29</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">25.72</td>
    <td align="right">25.70</td>
    <td align="right">25.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">18.35</td>
    <td align="right">18.47</td>
    <td align="right">18.45</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.11</td>
    <td align="right">18.88</td>
    <td align="right">19.01</td>
    <td align="right">18.83</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.97</td>
    <td align="right">8.72</td>
    <td align="right">8.72</td>
    <td align="right">9.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.58</td>
    <td align="right">26.52</td>
    <td align="right">26.53</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">26.92</td>
    <td align="right">26.97</td>
    <td align="right">26.95</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.77</td>
    <td align="right">13.75</td>
    <td align="right">13.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.17</td>
    <td align="right">35.29</td>
    <td align="right">35.29</td>
    <td align="right">35.28</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.65</td>
    <td align="right">34.17</td>
    <td align="right">34.47</td>
    <td align="right">34.35</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.83</td>
    <td align="right">17.82</td>
    <td align="right">17.81</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.57</td>
    <td align="right">38.31</td>
    <td align="right">38.29</td>
    <td align="right">38.27</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.40</td>
    <td align="right">41.25</td>
    <td align="right">41.15</td>
    <td align="right">41.10</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.11</td>
    <td align="right">19.76</td>
    <td align="right">19.74</td>
    <td align="right">19.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.68</td>
    <td align="right">8.48</td>
    <td align="right">8.68</td>
    <td align="right">8.50</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">18.32</td>
    <td align="right">18.33</td>
    <td align="right">18.31</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.09</td>
    <td align="right">18.86</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.89</td>
    <td align="right">14.09</td>
    <td align="right">14.08</td>
    <td align="right">14.09</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.66</td>
    <td align="right">26.58</td>
    <td align="right">26.54</td>
    <td align="right">26.56</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">26.93</td>
    <td align="right">26.96</td>
    <td align="right">26.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">17.21</td>
    <td align="right">17.23</td>
    <td align="right">17.20</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.20</td>
    <td align="right">35.45</td>
    <td align="right">35.30</td>
    <td align="right">35.29</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.62</td>
    <td align="right">34.22</td>
    <td align="right">34.33</td>
    <td align="right">34.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">20.14</td>
    <td align="right">19.99</td>
    <td align="right">19.99</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">38.32</td>
    <td align="right">38.29</td>
    <td align="right">38.31</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.39</td>
    <td align="right">41.26</td>
    <td align="right">41.19</td>
    <td align="right">41.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.23</td>
    <td align="right">20.02</td>
    <td align="right">20.04</td>
    <td align="right">20.04</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.31</td>
    <td align="right">39.17</td>
    <td align="right">37.62</td>
    <td align="right">37.73</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">28.29</td>
    <td align="right">27.87</td>
    <td align="right">27.80</td>
    <td align="right">27.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.99</td>
    <td align="right">28.43</td>
    <td align="right">28.41</td>
    <td align="right">28.43</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.65</td>
    <td align="right">44.02</td>
    <td align="right">45.34</td>
    <td align="right">44.12</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.70</td>
    <td align="right">36.65</td>
    <td align="right">36.64</td>
    <td align="right">36.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.14</td>
    <td align="right">34.28</td>
    <td align="right">34.27</td>
    <td align="right">34.28</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.13</td>
    <td align="right">48.35</td>
    <td align="right">48.87</td>
    <td align="right">48.72</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.49</td>
    <td align="right">38.78</td>
    <td align="right">38.65</td>
    <td align="right">38.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.71</td>
    <td align="right">39.28</td>
    <td align="right">39.28</td>
    <td align="right">39.27</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.50</td>
    <td align="right">52.58</td>
    <td align="right">52.77</td>
    <td align="right">52.61</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">51.98</td>
    <td align="right">50.52</td>
    <td align="right">50.82</td>
    <td align="right">50.63</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">125.28</td>
    <td align="right">62.59</td>
    <td align="right">23.38</td>
    <td align="right">33.25</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.52</td>
    <td align="right">34.64</td>
    <td align="right">34.33</td>
    <td align="right">35.44</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.31</td>
    <td align="right">15.86</td>
    <td align="right">15.81</td>
    <td align="right">15.78</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.62</td>
    <td align="right">21.58</td>
    <td align="right">21.56</td>
    <td align="right">21.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">79.97</td>
    <td align="right">99.13</td>
    <td align="right">48.38</td>
    <td align="right">54.19</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">27.34</td>
    <td align="right">29.36</td>
    <td align="right">29.31</td>
    <td align="right">29.33</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.68</td>
    <td align="right">34.59</td>
    <td align="right">34.61</td>
    <td align="right">34.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">145.39</td>
    <td align="right">208.78</td>
    <td align="right">67.73</td>
    <td align="right">84.49</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.93</td>
    <td align="right">49.26</td>
    <td align="right">49.17</td>
    <td align="right">49.17</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.56</td>
    <td align="right">51.55</td>
    <td align="right">51.41</td>
    <td align="right">51.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.21</td>
    <td align="right">322.83</td>
    <td align="right">84.69</td>
    <td align="right">107.83</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">65.27</td>
    <td align="right">66.55</td>
    <td align="right">66.43</td>
    <td align="right">66.42</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.52</td>
    <td align="right">70.48</td>
    <td align="right">70.47</td>
    <td align="right">70.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.24</td>
    <td align="right">21.66</td>
    <td align="right">21.74</td>
    <td align="right">21.87</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.20</td>
    <td align="right">22.71</td>
    <td align="right">22.77</td>
    <td align="right">22.72</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.84</td>
    <td align="right">11.80</td>
    <td align="right">11.78</td>
    <td align="right">11.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.92</td>
    <td align="right">40.21</td>
    <td align="right">40.15</td>
    <td align="right">40.20</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.30</td>
    <td align="right">40.66</td>
    <td align="right">40.78</td>
    <td align="right">40.75</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.36</td>
    <td align="right">25.14</td>
    <td align="right">24.07</td>
    <td align="right">24.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.66</td>
    <td align="right">70.99</td>
    <td align="right">70.87</td>
    <td align="right">70.87</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.29</td>
    <td align="right">69.03</td>
    <td align="right">68.91</td>
    <td align="right">69.14</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">39.01</td>
    <td align="right">41.91</td>
    <td align="right">41.45</td>
    <td align="right">41.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.10</td>
    <td align="right">88.28</td>
    <td align="right">88.27</td>
    <td align="right">88.27</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">98.30</td>
    <td align="right">93.98</td>
    <td align="right">94.39</td>
    <td align="right">95.16</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">54.21</td>
    <td align="right">53.14</td>
    <td align="right">53.30</td>
    <td align="right">53.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.39</td>
    <td align="right">11.03</td>
    <td align="right">11.02</td>
    <td align="right">10.70</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.35</td>
    <td align="right">21.91</td>
    <td align="right">21.83</td>
    <td align="right">22.04</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.17</td>
    <td align="right">22.90</td>
    <td align="right">22.91</td>
    <td align="right">22.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.11</td>
    <td align="right">25.49</td>
    <td align="right">25.27</td>
    <td align="right">25.16</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.85</td>
    <td align="right">39.83</td>
    <td align="right">39.75</td>
    <td align="right">39.75</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.01</td>
    <td align="right">46.26</td>
    <td align="right">46.17</td>
    <td align="right">46.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.45</td>
    <td align="right">41.00</td>
    <td align="right">40.99</td>
    <td align="right">41.12</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.20</td>
    <td align="right">70.08</td>
    <td align="right">70.19</td>
    <td align="right">70.26</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.50</td>
    <td align="right">69.92</td>
    <td align="right">70.03</td>
    <td align="right">70.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">54.05</td>
    <td align="right">55.07</td>
    <td align="right">55.15</td>
    <td align="right">55.12</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.89</td>
    <td align="right">89.91</td>
    <td align="right">89.90</td>
    <td align="right">89.90</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.53</td>
    <td align="right">92.37</td>
    <td align="right">92.57</td>
    <td align="right">93.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.35</td>
    <td align="right">23.72</td>
    <td align="right">23.61</td>
    <td align="right">23.72</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">48.65</td>
    <td align="right">40.39</td>
    <td align="right">38.92</td>
    <td align="right">38.98</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">39.78</td>
    <td align="right">34.79</td>
    <td align="right">34.81</td>
    <td align="right">33.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.34</td>
    <td align="right">42.08</td>
    <td align="right">42.04</td>
    <td align="right">42.01</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">66.28</td>
    <td align="right">59.90</td>
    <td align="right">60.70</td>
    <td align="right">60.15</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.39</td>
    <td align="right">58.68</td>
    <td align="right">58.69</td>
    <td align="right">58.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.47</td>
    <td align="right">63.14</td>
    <td align="right">63.08</td>
    <td align="right">63.08</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">92.38</td>
    <td align="right">81.49</td>
    <td align="right">81.72</td>
    <td align="right">81.71</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.57</td>
    <td align="right">81.83</td>
    <td align="right">81.85</td>
    <td align="right">81.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.30</td>
    <td align="right">81.22</td>
    <td align="right">81.02</td>
    <td align="right">81.21</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">111.07</td>
    <td align="right">100.63</td>
    <td align="right">100.54</td>
    <td align="right">100.64</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">126.52</td>
    <td align="right">117.12</td>
    <td align="right">116.82</td>
    <td align="right">116.95</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.99</td>
    <td align="right">6.61</td>
    <td align="right">5.57</td>
    <td align="right">7.35</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.76</td>
    <td align="right">60.31</td>
    <td align="right">39.85</td>
    <td align="right">43.03</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.90</td>
    <td align="right">20.51</td>
    <td align="right">23.29</td>
    <td align="right">24.04</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.80</td>
    <td align="right">24.61</td>
    <td align="right">26.27</td>
    <td align="right">27.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">98.61</td>
    <td align="right">87.59</td>
    <td align="right">42.07</td>
    <td align="right">45.12</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.43</td>
    <td align="right">22.12</td>
    <td align="right">24.28</td>
    <td align="right">25.17</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.39</td>
    <td align="right">27.53</td>
    <td align="right">28.22</td>
    <td align="right">29.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">121.24</td>
    <td align="right">104.79</td>
    <td align="right">41.37</td>
    <td align="right">47.26</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.09</td>
    <td align="right">25.83</td>
    <td align="right">25.95</td>
    <td align="right">27.37</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.86</td>
    <td align="right">30.19</td>
    <td align="right">29.92</td>
    <td align="right">31.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">156.56</td>
    <td align="right">134.56</td>
    <td align="right">41.14</td>
    <td align="right">51.31</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.53</td>
    <td align="right">26.74</td>
    <td align="right">27.32</td>
    <td align="right">28.25</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.73</td>
    <td align="right">31.74</td>
    <td align="right">31.93</td>
    <td align="right">32.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.33</td>
    <td align="right">41.70</td>
    <td align="right">41.63</td>
    <td align="right">42.73</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.44</td>
    <td align="right">42.93</td>
    <td align="right">41.58</td>
    <td align="right">41.62</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.69</td>
    <td align="right">28.25</td>
    <td align="right">28.05</td>
    <td align="right">28.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.30</td>
    <td align="right">56.05</td>
    <td align="right">56.32</td>
    <td align="right">56.31</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">31.88</td>
    <td align="right">56.24</td>
    <td align="right">57.23</td>
    <td align="right">57.42</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.76</td>
    <td align="right">37.26</td>
    <td align="right">37.39</td>
    <td align="right">37.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.67</td>
    <td align="right">76.10</td>
    <td align="right">76.49</td>
    <td align="right">75.83</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.14</td>
    <td align="right">75.65</td>
    <td align="right">75.62</td>
    <td align="right">75.52</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.05</td>
    <td align="right">47.24</td>
    <td align="right">47.24</td>
    <td align="right">47.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.10</td>
    <td align="right">86.73</td>
    <td align="right">84.75</td>
    <td align="right">84.77</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.16</td>
    <td align="right">88.60</td>
    <td align="right">88.62</td>
    <td align="right">90.97</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.06</td>
    <td align="right">47.54</td>
    <td align="right">47.42</td>
    <td align="right">47.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.84</td>
    <td align="right">28.16</td>
    <td align="right">27.74</td>
    <td align="right">27.72</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.68</td>
    <td align="right">30.16</td>
    <td align="right">30.15</td>
    <td align="right">30.15</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.33</td>
    <td align="right">30.33</td>
    <td align="right">30.32</td>
    <td align="right">30.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.92</td>
    <td align="right">37.49</td>
    <td align="right">37.41</td>
    <td align="right">37.41</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.80</td>
    <td align="right">37.98</td>
    <td align="right">37.73</td>
    <td align="right">37.73</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.66</td>
    <td align="right">38.84</td>
    <td align="right">38.65</td>
    <td align="right">38.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.07</td>
    <td align="right">47.37</td>
    <td align="right">47.09</td>
    <td align="right">47.09</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.86</td>
    <td align="right">50.17</td>
    <td align="right">49.88</td>
    <td align="right">49.94</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.71</td>
    <td align="right">49.80</td>
    <td align="right">49.62</td>
    <td align="right">49.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.09</td>
    <td align="right">47.67</td>
    <td align="right">47.41</td>
    <td align="right">47.35</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.60</td>
    <td align="right">52.41</td>
    <td align="right">52.13</td>
    <td align="right">52.12</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.93</td>
    <td align="right">52.13</td>
    <td align="right">51.87</td>
    <td align="right">51.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">26.92</td>
    <td align="right">41.75</td>
    <td align="right">42.02</td>
    <td align="right">42.05</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.50</td>
    <td align="right">47.30</td>
    <td align="right">47.44</td>
    <td align="right">47.23</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.15</td>
    <td align="right">60.42</td>
    <td align="right">60.48</td>
    <td align="right">60.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.50</td>
    <td align="right">57.00</td>
    <td align="right">56.93</td>
    <td align="right">56.65</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.89</td>
    <td align="right">60.22</td>
    <td align="right">59.92</td>
    <td align="right">59.98</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.51</td>
    <td align="right">78.19</td>
    <td align="right">78.16</td>
    <td align="right">79.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.54</td>
    <td align="right">67.14</td>
    <td align="right">67.09</td>
    <td align="right">67.19</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.90</td>
    <td align="right">77.31</td>
    <td align="right">77.25</td>
    <td align="right">77.33</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">48.22</td>
    <td align="right">86.73</td>
    <td align="right">82.84</td>
    <td align="right">84.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.20</td>
    <td align="right">92.48</td>
    <td align="right">93.54</td>
    <td align="right">92.85</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.36</td>
    <td align="right">93.05</td>
    <td align="right">93.72</td>
    <td align="right">93.30</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">65.57</td>
    <td align="right">117.03</td>
    <td align="right">117.10</td>
    <td align="right">117.08</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.20</td>
    <td align="right">33.60</td>
    <td align="right">15.79</td>
    <td align="right">24.18</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.33</td>
    <td align="right">61.94</td>
    <td align="right">41.23</td>
    <td align="right">44.50</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.13</td>
    <td align="right">20.52</td>
    <td align="right">23.61</td>
    <td align="right">24.67</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.58</td>
    <td align="right">26.69</td>
    <td align="right">28.11</td>
    <td align="right">29.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">109.17</td>
    <td align="right">91.41</td>
    <td align="right">44.56</td>
    <td align="right">48.47</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.21</td>
    <td align="right">24.25</td>
    <td align="right">26.05</td>
    <td align="right">27.35</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.85</td>
    <td align="right">30.70</td>
    <td align="right">31.37</td>
    <td align="right">32.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">262.49</td>
    <td align="right">219.17</td>
    <td align="right">64.88</td>
    <td align="right">81.11</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.96</td>
    <td align="right">38.00</td>
    <td align="right">38.59</td>
    <td align="right">40.20</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.34</td>
    <td align="right">50.03</td>
    <td align="right">48.61</td>
    <td align="right">49.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">438.25</td>
    <td align="right">352.95</td>
    <td align="right">78.35</td>
    <td align="right">108.96</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.27</td>
    <td align="right">44.88</td>
    <td align="right">45.65</td>
    <td align="right">46.86</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.31</td>
    <td align="right">63.12</td>
    <td align="right">61.61</td>
    <td align="right">64.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.00</td>
    <td align="right">41.86</td>
    <td align="right">41.77</td>
    <td align="right">42.89</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.42</td>
    <td align="right">43.11</td>
    <td align="right">41.86</td>
    <td align="right">41.96</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.13</td>
    <td align="right">30.30</td>
    <td align="right">30.30</td>
    <td align="right">30.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.21</td>
    <td align="right">57.98</td>
    <td align="right">58.46</td>
    <td align="right">58.34</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">35.75</td>
    <td align="right">58.92</td>
    <td align="right">60.17</td>
    <td align="right">59.83</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.52</td>
    <td align="right">40.60</td>
    <td align="right">40.81</td>
    <td align="right">40.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">58.14</td>
    <td align="right">90.04</td>
    <td align="right">90.42</td>
    <td align="right">89.87</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">65.16</td>
    <td align="right">92.71</td>
    <td align="right">92.67</td>
    <td align="right">92.83</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">47.55</td>
    <td align="right">72.98</td>
    <td align="right">73.18</td>
    <td align="right">73.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.59</td>
    <td align="right">109.87</td>
    <td align="right">108.23</td>
    <td align="right">108.25</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.13</td>
    <td align="right">118.10</td>
    <td align="right">118.02</td>
    <td align="right">120.17</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">59.30</td>
    <td align="right">86.22</td>
    <td align="right">86.17</td>
    <td align="right">86.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.13</td>
    <td align="right">29.88</td>
    <td align="right">29.88</td>
    <td align="right">29.88</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.09</td>
    <td align="right">31.97</td>
    <td align="right">31.97</td>
    <td align="right">31.99</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.56</td>
    <td align="right">31.86</td>
    <td align="right">31.86</td>
    <td align="right">31.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.08</td>
    <td align="right">40.56</td>
    <td align="right">40.78</td>
    <td align="right">40.96</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.78</td>
    <td align="right">40.80</td>
    <td align="right">40.83</td>
    <td align="right">40.56</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">22.99</td>
    <td align="right">42.39</td>
    <td align="right">42.25</td>
    <td align="right">42.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">51.02</td>
    <td align="right">73.42</td>
    <td align="right">73.48</td>
    <td align="right">73.03</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.12</td>
    <td align="right">73.91</td>
    <td align="right">73.84</td>
    <td align="right">73.96</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">54.14</td>
    <td align="right">74.23</td>
    <td align="right">74.03</td>
    <td align="right">74.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.81</td>
    <td align="right">87.01</td>
    <td align="right">86.45</td>
    <td align="right">86.19</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.91</td>
    <td align="right">90.38</td>
    <td align="right">90.25</td>
    <td align="right">90.25</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">65.53</td>
    <td align="right">90.37</td>
    <td align="right">90.24</td>
    <td align="right">90.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.63</td>
    <td align="right">41.87</td>
    <td align="right">42.29</td>
    <td align="right">42.16</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.27</td>
    <td align="right">47.69</td>
    <td align="right">48.01</td>
    <td align="right">47.73</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.33</td>
    <td align="right">60.66</td>
    <td align="right">60.76</td>
    <td align="right">60.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.29</td>
    <td align="right">59.18</td>
    <td align="right">58.67</td>
    <td align="right">58.39</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">44.62</td>
    <td align="right">65.26</td>
    <td align="right">64.88</td>
    <td align="right">65.31</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">47.69</td>
    <td align="right">79.09</td>
    <td align="right">78.99</td>
    <td align="right">80.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">58.41</td>
    <td align="right">75.87</td>
    <td align="right">76.02</td>
    <td align="right">75.96</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.63</td>
    <td align="right">104.30</td>
    <td align="right">104.57</td>
    <td align="right">104.15</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">78.28</td>
    <td align="right">105.98</td>
    <td align="right">103.50</td>
    <td align="right">104.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">80.25</td>
    <td align="right">111.25</td>
    <td align="right">111.54</td>
    <td align="right">111.03</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.86</td>
    <td align="right">128.34</td>
    <td align="right">128.46</td>
    <td align="right">128.42</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">110.76</td>
    <td align="right">145.03</td>
    <td align="right">145.12</td>
    <td align="right">145.07</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
