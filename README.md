# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
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
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.56</td>
    <td align="right">4.87</td>
    <td align="right">4.09</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.99</td>
    <td align="right">11.39</td>
    <td align="right">17.54</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.71</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.22</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">15.32</td>
    <td align="right">17.20</td>
    <td align="right">18.85</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.24</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.82</td>
    <td align="right">5.28</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">18.85</td>
    <td align="right">20.26</td>
    <td align="right">17.47</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.74</td>
    <td align="right">5.24</td>
    <td align="right">5.25</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.27</td>
    <td align="right">5.84</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">23.28</td>
    <td align="right">24.83</td>
    <td align="right">18.01</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.07</td>
    <td align="right">5.83</td>
    <td align="right">5.83</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.65</td>
    <td align="right">6.14</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.67</td>
    <td align="right">5.45</td>
    <td align="right">5.45</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.18</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.20</td>
    <td align="right">2.83</td>
    <td align="right">2.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.96</td>
    <td align="right">9.35</td>
    <td align="right">9.34</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.75</td>
    <td align="right">9.43</td>
    <td align="right">9.43</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.16</td>
    <td align="right">11.52</td>
    <td align="right">11.52</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">21.01</td>
    <td align="right">14.02</td>
    <td align="right">14.04</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.44</td>
    <td align="right">4.85</td>
    <td align="right">3.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.77</td>
    <td align="right">13.03</td>
    <td align="right">13.02</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.92</td>
    <td align="right">15.21</td>
    <td align="right">15.21</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.49</td>
    <td align="right">4.89</td>
    <td align="right">3.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.21</td>
    <td align="right">2.70</td>
    <td align="right">2.66</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.60</td>
    <td align="right">4.65</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.79</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.38</td>
    <td align="right">2.77</td>
    <td align="right">2.73</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.41</td>
    <td align="right">4.02</td>
    <td align="right">4.04</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.79</td>
    <td align="right">4.59</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.63</td>
    <td align="right">4.75</td>
    <td align="right">3.52</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.67</td>
    <td align="right">7.03</td>
    <td align="right">5.73</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.06</td>
    <td align="right">6.93</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.68</td>
    <td align="right">4.78</td>
    <td align="right">3.52</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.36</td>
    <td align="right">8.49</td>
    <td align="right">5.77</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">9.01</td>
    <td align="right">8.39</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.18</td>
    <td align="right">7.30</td>
    <td align="right">14.98</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.65</td>
    <td align="right">8.60</td>
    <td align="right">18.57</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.25</td>
    <td align="right">11.26</td>
    <td align="right">11.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.14</td>
    <td align="right">9.87</td>
    <td align="right">13.81</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.58</td>
    <td align="right">10.19</td>
    <td align="right">15.68</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.52</td>
    <td align="right">14.27</td>
    <td align="right">14.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.09</td>
    <td align="right">11.46</td>
    <td align="right">13.48</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.85</td>
    <td align="right">12.61</td>
    <td align="right">16.79</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">15.77</td>
    <td align="right">15.99</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">12.98</td>
    <td align="right">13.91</td>
    <td align="right">14.70</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.76</td>
    <td align="right">14.59</td>
    <td align="right">16.16</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">20.45</td>
    <td align="right">21.09</td>
    <td align="right">21.02</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.35</td>
    <td align="right">23.51</td>
    <td align="right">14.45</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">17.93</td>
    <td align="right">19.80</td>
    <td align="right">21.10</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.00</td>
    <td align="right">5.65</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.54</td>
    <td align="right">6.26</td>
    <td align="right">6.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">41.30</td>
    <td align="right">47.88</td>
    <td align="right">25.56</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.31</td>
    <td align="right">10.90</td>
    <td align="right">10.89</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.95</td>
    <td align="right">12.87</td>
    <td align="right">12.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">73.68</td>
    <td align="right">81.57</td>
    <td align="right">30.72</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.46</td>
    <td align="right">18.01</td>
    <td align="right">18.00</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">18.49</td>
    <td align="right">19.00</td>
    <td align="right">19.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">109.09</td>
    <td align="right">118.14</td>
    <td align="right">36.39</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.41</td>
    <td align="right">21.87</td>
    <td align="right">21.88</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">22.65</td>
    <td align="right">22.65</td>
    <td align="right">22.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.66</td>
    <td align="right">7.61</td>
    <td align="right">7.62</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.96</td>
    <td align="right">8.73</td>
    <td align="right">8.79</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.85</td>
    <td align="right">3.40</td>
    <td align="right">3.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.09</td>
    <td align="right">16.58</td>
    <td align="right">16.55</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.83</td>
    <td align="right">18.14</td>
    <td align="right">18.11</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.77</td>
    <td align="right">7.79</td>
    <td align="right">8.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">29.60</td>
    <td align="right">30.72</td>
    <td align="right">30.69</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">35.56</td>
    <td align="right">33.93</td>
    <td align="right">33.88</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">18.43</td>
    <td align="right">17.59</td>
    <td align="right">13.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">38.66</td>
    <td align="right">39.79</td>
    <td align="right">39.82</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">41.24</td>
    <td align="right">50.71</td>
    <td align="right">50.70</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">21.43</td>
    <td align="right">20.04</td>
    <td align="right">14.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">4.81</td>
    <td align="right">4.40</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.77</td>
    <td align="right">5.91</td>
    <td align="right">5.97</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">9.36</td>
    <td align="right">9.80</td>
    <td align="right">9.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.76</td>
    <td align="right">7.45</td>
    <td align="right">7.41</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">9.17</td>
    <td align="right">10.03</td>
    <td align="right">9.98</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.96</td>
    <td align="right">12.20</td>
    <td align="right">12.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.57</td>
    <td align="right">17.62</td>
    <td align="right">13.15</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.77</td>
    <td align="right">22.57</td>
    <td align="right">19.31</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.73</td>
    <td align="right">22.69</td>
    <td align="right">19.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.34</td>
    <td align="right">20.07</td>
    <td align="right">14.64</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.71</td>
    <td align="right">30.97</td>
    <td align="right">22.27</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">30.14</td>
    <td align="right">31.16</td>
    <td align="right">22.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.12</td>
    <td align="right">8.25</td>
    <td align="right">15.94</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.10</td>
    <td align="right">10.31</td>
    <td align="right">20.20</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">14.39</td>
    <td align="right">14.96</td>
    <td align="right">14.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">16.93</td>
    <td align="right">17.05</td>
    <td align="right">17.74</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">21.90</td>
    <td align="right">20.29</td>
    <td align="right">19.55</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">30.23</td>
    <td align="right">30.62</td>
    <td align="right">30.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.77</td>
    <td align="right">27.50</td>
    <td align="right">21.13</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">34.97</td>
    <td align="right">33.50</td>
    <td align="right">26.01</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">45.88</td>
    <td align="right">50.09</td>
    <td align="right">50.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">41.77</td>
    <td align="right">41.70</td>
    <td align="right">24.89</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">50.78</td>
    <td align="right">50.02</td>
    <td align="right">27.41</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.95</td>
    <td align="right">73.33</td>
    <td align="right">73.51</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.18</td>
    <td align="right">6.31</td>
    <td align="right">4.34</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.33</td>
    <td align="right">10.49</td>
    <td align="right">16.96</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.40</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.93</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.13</td>
    <td align="right">15.30</td>
    <td align="right">18.23</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.91</td>
    <td align="right">4.53</td>
    <td align="right">4.52</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.36</td>
    <td align="right">5.15</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.03</td>
    <td align="right">18.69</td>
    <td align="right">16.94</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.30</td>
    <td align="right">5.17</td>
    <td align="right">5.17</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.85</td>
    <td align="right">5.56</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.47</td>
    <td align="right">23.17</td>
    <td align="right">17.74</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.79</td>
    <td align="right">5.55</td>
    <td align="right">5.54</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.31</td>
    <td align="right">3.38</td>
    <td align="right">3.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.13</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.25</td>
    <td align="right">3.59</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.83</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.96</td>
    <td align="right">4.70</td>
    <td align="right">4.71</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.97</td>
    <td align="right">4.82</td>
    <td align="right">4.83</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.24</td>
    <td align="right">2.31</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.66</td>
    <td align="right">7.42</td>
    <td align="right">7.52</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.95</td>
    <td align="right">7.29</td>
    <td align="right">7.29</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.31</td>
    <td align="right">4.33</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.09</td>
    <td align="right">8.27</td>
    <td align="right">8.27</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.80</td>
    <td align="right">8.44</td>
    <td align="right">8.39</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.36</td>
    <td align="right">4.35</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.81</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.85</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.96</td>
    <td align="right">3.92</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.86</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.16</td>
    <td align="right">3.80</td>
    <td align="right">3.81</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.11</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.43</td>
    <td align="right">4.08</td>
    <td align="right">3.03</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.74</td>
    <td align="right">6.05</td>
    <td align="right">5.08</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.97</td>
    <td align="right">5.90</td>
    <td align="right">4.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.48</td>
    <td align="right">4.10</td>
    <td align="right">3.02</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.91</td>
    <td align="right">7.19</td>
    <td align="right">5.11</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.25</td>
    <td align="right">7.02</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">5.81</td>
    <td align="right">6.53</td>
    <td align="right">14.60</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">13.05</td>
    <td align="right">7.71</td>
    <td align="right">18.08</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.37</td>
    <td align="right">10.33</td>
    <td align="right">10.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.52</td>
    <td align="right">9.00</td>
    <td align="right">13.38</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.70</td>
    <td align="right">9.12</td>
    <td align="right">15.22</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.48</td>
    <td align="right">13.88</td>
    <td align="right">13.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.53</td>
    <td align="right">10.60</td>
    <td align="right">12.97</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.51</td>
    <td align="right">11.81</td>
    <td align="right">16.33</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">15.85</td>
    <td align="right">15.22</td>
    <td align="right">15.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">13.50</td>
    <td align="right">13.21</td>
    <td align="right">13.99</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.61</td>
    <td align="right">13.48</td>
    <td align="right">15.59</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.50</td>
    <td align="right">20.72</td>
    <td align="right">20.82</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">51.95</td>
    <td align="right">23.60</td>
    <td align="right">14.43</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.05</td>
    <td align="right">12.15</td>
    <td align="right">18.88</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.58</td>
    <td align="right">5.18</td>
    <td align="right">5.17</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.46</td>
    <td align="right">6.10</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">37.58</td>
    <td align="right">39.29</td>
    <td align="right">24.06</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.97</td>
    <td align="right">9.78</td>
    <td align="right">9.83</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.78</td>
    <td align="right">13.05</td>
    <td align="right">13.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">72.64</td>
    <td align="right">74.04</td>
    <td align="right">29.99</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.97</td>
    <td align="right">17.81</td>
    <td align="right">17.81</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.71</td>
    <td align="right">18.41</td>
    <td align="right">18.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">104.93</td>
    <td align="right">103.47</td>
    <td align="right">35.32</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.35</td>
    <td align="right">21.51</td>
    <td align="right">21.49</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.74</td>
    <td align="right">15.15</td>
    <td align="right">15.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.21</td>
    <td align="right">4.89</td>
    <td align="right">4.89</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.73</td>
    <td align="right">5.35</td>
    <td align="right">5.39</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.54</td>
    <td align="right">3.37</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.77</td>
    <td align="right">9.98</td>
    <td align="right">9.94</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.47</td>
    <td align="right">10.76</td>
    <td align="right">10.77</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.91</td>
    <td align="right">7.13</td>
    <td align="right">7.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.53</td>
    <td align="right">22.30</td>
    <td align="right">22.32</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.27</td>
    <td align="right">22.01</td>
    <td align="right">22.06</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.76</td>
    <td align="right">15.96</td>
    <td align="right">11.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.80</td>
    <td align="right">29.77</td>
    <td align="right">29.77</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.73</td>
    <td align="right">30.78</td>
    <td align="right">30.79</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">17.22</td>
    <td align="right">18.15</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.74</td>
    <td align="right">3.47</td>
    <td align="right">3.38</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.66</td>
    <td align="right">5.02</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.96</td>
    <td align="right">5.22</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.42</td>
    <td align="right">7.42</td>
    <td align="right">7.44</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.72</td>
    <td align="right">9.93</td>
    <td align="right">9.87</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.55</td>
    <td align="right">10.88</td>
    <td align="right">10.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.64</td>
    <td align="right">15.93</td>
    <td align="right">11.90</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.10</td>
    <td align="right">21.39</td>
    <td align="right">17.22</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">18.70</td>
    <td align="right">20.79</td>
    <td align="right">16.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">16.51</td>
    <td align="right">17.69</td>
    <td align="right">13.18</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">25.05</td>
    <td align="right">26.66</td>
    <td align="right">19.42</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.57</td>
    <td align="right">27.20</td>
    <td align="right">19.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.09</td>
    <td align="right">7.89</td>
    <td align="right">15.85</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">14.65</td>
    <td align="right">10.71</td>
    <td align="right">20.10</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.41</td>
    <td align="right">16.32</td>
    <td align="right">16.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">15.40</td>
    <td align="right">14.95</td>
    <td align="right">17.09</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">23.05</td>
    <td align="right">19.29</td>
    <td align="right">19.43</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">27.51</td>
    <td align="right">27.90</td>
    <td align="right">27.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.80</td>
    <td align="right">26.79</td>
    <td align="right">21.15</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">35.66</td>
    <td align="right">32.52</td>
    <td align="right">24.43</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">47.28</td>
    <td align="right">47.36</td>
    <td align="right">47.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">36.49</td>
    <td align="right">35.21</td>
    <td align="right">23.78</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">50.56</td>
    <td align="right">39.68</td>
    <td align="right">25.68</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">76.98</td>
    <td align="right">74.19</td>
    <td align="right">72.63</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.60</td>
    <td align="right">2.49</td>
    <td align="right">1.97</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">6.30</td>
    <td align="right">4.43</td>
    <td align="right">11.38</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.31</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.45</td>
    <td align="right">6.62</td>
    <td align="right">11.77</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.37</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.70</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.41</td>
    <td align="right">8.19</td>
    <td align="right">10.99</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.75</td>
    <td align="right">1.57</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.53</td>
    <td align="right">10.69</td>
    <td align="right">11.27</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.72</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.24</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.26</td>
    <td align="right">1.74</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.01</td>
    <td align="right">1.70</td>
    <td align="right">1.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.15</td>
    <td align="right">1.85</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.72</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.51</td>
    <td align="right">1.34</td>
    <td align="right">1.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.19</td>
    <td align="right">2.92</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.01</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.89</td>
    <td align="right">2.37</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.65</td>
    <td align="right">3.33</td>
    <td align="right">3.35</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.80</td>
    <td align="right">3.58</td>
    <td align="right">3.58</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="right">1.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.02</td>
    <td align="right">1.71</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.29</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.33</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.07</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.17</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.83</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.96</td>
    <td align="right">2.39</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.07</td>
    <td align="right">2.96</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.03</td>
    <td align="right">3.02</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.89</td>
    <td align="right">2.86</td>
    <td align="right">1.72</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.57</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.79</td>
    <td align="right">3.59</td>
    <td align="right">3.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.13</td>
    <td align="right">3.17</td>
    <td align="right">10.11</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.00</td>
    <td align="right">3.95</td>
    <td align="right">12.62</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">7.70</td>
    <td align="right">4.86</td>
    <td align="right">4.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.26</td>
    <td align="right">4.29</td>
    <td align="right">9.89</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">7.47</td>
    <td align="right">4.56</td>
    <td align="right">10.48</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">10.95</td>
    <td align="right">6.92</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">5.38</td>
    <td align="right">5.17</td>
    <td align="right">9.62</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">8.61</td>
    <td align="right">5.78</td>
    <td align="right">11.21</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.06</td>
    <td align="right">7.55</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">6.86</td>
    <td align="right">6.23</td>
    <td align="right">10.11</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">9.41</td>
    <td align="right">6.33</td>
    <td align="right">10.73</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">17.67</td>
    <td align="right">10.65</td>
    <td align="right">10.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.43</td>
    <td align="right">11.07</td>
    <td align="right">5.91</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">7.70</td>
    <td align="right">6.28</td>
    <td align="right">12.95</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.03</td>
    <td align="right">1.95</td>
    <td align="right">1.96</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.16</td>
    <td align="right">2.08</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.87</td>
    <td align="right">11.60</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.17</td>
    <td align="right">3.30</td>
    <td align="right">3.36</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.31</td>
    <td align="right">3.26</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">31.00</td>
    <td align="right">24.70</td>
    <td align="right">17.80</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.71</td>
    <td align="right">6.30</td>
    <td align="right">6.15</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.48</td>
    <td align="right">5.97</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.64</td>
    <td align="right">40.64</td>
    <td align="right">20.83</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.03</td>
    <td align="right">7.69</td>
    <td align="right">8.23</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.64</td>
    <td align="right">6.90</td>
    <td align="right">6.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.72</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.73</td>
    <td align="right">2.60</td>
    <td align="right">2.62</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.40</td>
    <td align="right">2.53</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.75</td>
    <td align="right">4.35</td>
    <td align="right">4.48</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.53</td>
    <td align="right">4.66</td>
    <td align="right">4.63</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.59</td>
    <td align="right">3.23</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.68</td>
    <td align="right">9.52</td>
    <td align="right">9.52</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.24</td>
    <td align="right">9.76</td>
    <td align="right">9.71</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.43</td>
    <td align="right">8.37</td>
    <td align="right">5.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.81</td>
    <td align="right">13.35</td>
    <td align="right">13.03</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.84</td>
    <td align="right">13.16</td>
    <td align="right">13.11</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.69</td>
    <td align="right">10.55</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.36</td>
    <td align="right">2.51</td>
    <td align="right">2.57</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.76</td>
    <td align="right">2.57</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.74</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.06</td>
    <td align="right">3.31</td>
    <td align="right">3.30</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.29</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.30</td>
    <td align="right">4.64</td>
    <td align="right">4.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.88</td>
    <td align="right">7.56</td>
    <td align="right">5.23</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.02</td>
    <td align="right">9.89</td>
    <td align="right">10.02</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.01</td>
    <td align="right">9.73</td>
    <td align="right">9.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.39</td>
    <td align="right">11.11</td>
    <td align="right">6.81</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.92</td>
    <td align="right">13.11</td>
    <td align="right">13.23</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.74</td>
    <td align="right">13.81</td>
    <td align="right">14.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">4.52</td>
    <td align="right">4.25</td>
    <td align="right">11.30</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.87</td>
    <td align="right">5.00</td>
    <td align="right">13.51</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">9.00</td>
    <td align="right">6.90</td>
    <td align="right">6.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">7.90</td>
    <td align="right">7.12</td>
    <td align="right">11.88</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.90</td>
    <td align="right">8.07</td>
    <td align="right">13.00</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">14.80</td>
    <td align="right">12.35</td>
    <td align="right">12.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.66</td>
    <td align="right">13.89</td>
    <td align="right">14.14</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">24.04</td>
    <td align="right">15.92</td>
    <td align="right">16.06</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.35</td>
    <td align="right">22.78</td>
    <td align="right">22.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">22.65</td>
    <td align="right">18.07</td>
    <td align="right">15.36</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">30.31</td>
    <td align="right">21.24</td>
    <td align="right">17.28</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">49.75</td>
    <td align="right">38.85</td>
    <td align="right">38.70</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.17</td>
    <td align="right">5.16</td>
    <td align="right">3.71</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.35</td>
    <td align="right">10.52</td>
    <td align="right">14.34</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.73</td>
    <td align="right">3.47</td>
    <td align="right">3.44</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.29</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.61</td>
    <td align="right">14.89</td>
    <td align="right">14.86</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.37</td>
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.94</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.33</td>
    <td align="right">18.31</td>
    <td align="right">13.95</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.93</td>
    <td align="right">4.27</td>
    <td align="right">4.26</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.63</td>
    <td align="right">5.13</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.40</td>
    <td align="right">22.82</td>
    <td align="right">14.15</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.62</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.17</td>
    <td align="right">5.53</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.29</td>
    <td align="right">4.24</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">7.86</td>
    <td align="right">4.56</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.23</td>
    <td align="right">7.03</td>
    <td align="right">7.02</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.94</td>
    <td align="right">6.85</td>
    <td align="right">6.86</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.78</td>
    <td align="right">2.90</td>
    <td align="right">2.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.53</td>
    <td align="right">9.23</td>
    <td align="right">9.06</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.47</td>
    <td align="right">10.37</td>
    <td align="right">10.28</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.27</td>
    <td align="right">4.39</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.59</td>
    <td align="right">10.33</td>
    <td align="right">10.31</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.18</td>
    <td align="right">12.28</td>
    <td align="right">12.22</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.32</td>
    <td align="right">4.42</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.84</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.71</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.77</td>
    <td align="right">2.99</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.21</td>
    <td align="right">3.23</td>
    <td align="right">2.58</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.21</td>
    <td align="right">3.80</td>
    <td align="right">3.17</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.02</td>
    <td align="right">4.51</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.38</td>
    <td align="right">4.23</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.84</td>
    <td align="right">6.35</td>
    <td align="right">4.86</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.26</td>
    <td align="right">6.20</td>
    <td align="right">4.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.43</td>
    <td align="right">4.25</td>
    <td align="right">2.92</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.35</td>
    <td align="right">6.82</td>
    <td align="right">4.83</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.68</td>
    <td align="right">6.71</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.90</td>
    <td align="right">6.57</td>
    <td align="right">11.24</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">9.72</td>
    <td align="right">8.87</td>
    <td align="right">14.07</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.04</td>
    <td align="right">8.82</td>
    <td align="right">8.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.77</td>
    <td align="right">9.70</td>
    <td align="right">12.01</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.64</td>
    <td align="right">11.15</td>
    <td align="right">13.19</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">13.86</td>
    <td align="right">12.88</td>
    <td align="right">12.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.38</td>
    <td align="right">11.39</td>
    <td align="right">11.71</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.17</td>
    <td align="right">13.24</td>
    <td align="right">12.71</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">15.24</td>
    <td align="right">15.27</td>
    <td align="right">15.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.58</td>
    <td align="right">14.05</td>
    <td align="right">12.57</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.24</td>
    <td align="right">15.13</td>
    <td align="right">12.30</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">23.54</td>
    <td align="right">22.89</td>
    <td align="right">22.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.07</td>
    <td align="right">23.15</td>
    <td align="right">12.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.99</td>
    <td align="right">11.07</td>
    <td align="right">15.53</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.28</td>
    <td align="right">3.74</td>
    <td align="right">3.64</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.67</td>
    <td align="right">4.44</td>
    <td align="right">4.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.69</td>
    <td align="right">17.14</td>
    <td align="right">16.48</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.12</td>
    <td align="right">5.82</td>
    <td align="right">5.69</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.90</td>
    <td align="right">6.41</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">66.11</td>
    <td align="right">75.00</td>
    <td align="right">25.00</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.01</td>
    <td align="right">13.48</td>
    <td align="right">13.55</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.02</td>
    <td align="right">15.57</td>
    <td align="right">15.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.72</td>
    <td align="right">109.72</td>
    <td align="right">29.56</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.38</td>
    <td align="right">16.51</td>
    <td align="right">16.57</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.38</td>
    <td align="right">22.43</td>
    <td align="right">22.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.99</td>
    <td align="right">4.59</td>
    <td align="right">4.53</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.26</td>
    <td align="right">4.98</td>
    <td align="right">4.89</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.16</td>
    <td align="right">2.29</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.63</td>
    <td align="right">20.50</td>
    <td align="right">20.61</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.84</td>
    <td align="right">10.61</td>
    <td align="right">10.45</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.96</td>
    <td align="right">4.97</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.77</td>
    <td align="right">23.04</td>
    <td align="right">23.16</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">29.49</td>
    <td align="right">27.98</td>
    <td align="right">27.94</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.87</td>
    <td align="right">15.34</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">35.66</td>
    <td align="right">34.86</td>
    <td align="right">34.82</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">39.62</td>
    <td align="right">37.54</td>
    <td align="right">37.53</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.27</td>
    <td align="right">17.78</td>
    <td align="right">12.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.19</td>
    <td align="right">2.11</td>
    <td align="right">2.01</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.10</td>
    <td align="right">3.44</td>
    <td align="right">3.38</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.20</td>
    <td align="right">3.22</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.06</td>
    <td align="right">5.18</td>
    <td align="right">4.37</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.97</td>
    <td align="right">5.53</td>
    <td align="right">4.85</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.77</td>
    <td align="right">6.17</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.79</td>
    <td align="right">14.89</td>
    <td align="right">10.66</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.77</td>
    <td align="right">18.93</td>
    <td align="right">15.84</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">26.28</td>
    <td align="right">20.87</td>
    <td align="right">17.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.72</td>
    <td align="right">17.74</td>
    <td align="right">12.27</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.23</td>
    <td align="right">26.34</td>
    <td align="right">18.69</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.72</td>
    <td align="right">24.33</td>
    <td align="right">18.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.52</td>
    <td align="right">7.33</td>
    <td align="right">11.95</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">10.28</td>
    <td align="right">9.60</td>
    <td align="right">14.68</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">11.43</td>
    <td align="right">9.94</td>
    <td align="right">9.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.09</td>
    <td align="right">11.89</td>
    <td align="right">13.71</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.03</td>
    <td align="right">13.84</td>
    <td align="right">14.27</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">15.53</td>
    <td align="right">13.88</td>
    <td align="right">14.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">25.26</td>
    <td align="right">25.64</td>
    <td align="right">19.61</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">33.47</td>
    <td align="right">32.81</td>
    <td align="right">19.87</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">39.06</td>
    <td align="right">38.05</td>
    <td align="right">38.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">35.32</td>
    <td align="right">34.51</td>
    <td align="right">22.82</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">42.30</td>
    <td align="right">41.23</td>
    <td align="right">21.81</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.07</td>
    <td align="right">64.15</td>
    <td align="right">64.17</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.25</td>
    <td align="right">35.27</td>
    <td align="right">14.19</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.72</td>
    <td align="right">44.22</td>
    <td align="right">37.68</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.35</td>
    <td align="right">18.09</td>
    <td align="right">17.80</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.25</td>
    <td align="right">20.80</td>
    <td align="right">20.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.82</td>
    <td align="right">67.89</td>
    <td align="right">41.89</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.35</td>
    <td align="right">21.26</td>
    <td align="right">21.28</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.16</td>
    <td align="right">18.89</td>
    <td align="right">18.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">51.33</td>
    <td align="right">84.23</td>
    <td align="right">39.45</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.45</td>
    <td align="right">19.10</td>
    <td align="right">19.28</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.33</td>
    <td align="right">21.05</td>
    <td align="right">21.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.17</td>
    <td align="right">109.32</td>
    <td align="right">39.95</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.57</td>
    <td align="right">20.92</td>
    <td align="right">20.56</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.22</td>
    <td align="right">21.92</td>
    <td align="right">21.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.35</td>
    <td align="right">22.60</td>
    <td align="right">22.53</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.56</td>
    <td align="right">27.37</td>
    <td align="right">26.33</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.42</td>
    <td align="right">15.77</td>
    <td align="right">15.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.95</td>
    <td align="right">29.46</td>
    <td align="right">29.61</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.27</td>
    <td align="right">32.50</td>
    <td align="right">32.45</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.12</td>
    <td align="right">17.69</td>
    <td align="right">17.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.00</td>
    <td align="right">35.64</td>
    <td align="right">35.54</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.87</td>
    <td align="right">49.06</td>
    <td align="right">49.17</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.71</td>
    <td align="right">20.70</td>
    <td align="right">20.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.13</td>
    <td align="right">40.06</td>
    <td align="right">40.15</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.51</td>
    <td align="right">58.30</td>
    <td align="right">58.04</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">24.32</td>
    <td align="right">24.98</td>
    <td align="right">24.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.05</td>
    <td align="right">15.98</td>
    <td align="right">15.98</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.55</td>
    <td align="right">22.63</td>
    <td align="right">22.57</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.57</td>
    <td align="right">26.59</td>
    <td align="right">26.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.30</td>
    <td align="right">19.54</td>
    <td align="right">19.45</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.83</td>
    <td align="right">29.54</td>
    <td align="right">29.60</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.22</td>
    <td align="right">32.46</td>
    <td align="right">32.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">23.02</td>
    <td align="right">23.80</td>
    <td align="right">23.83</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.89</td>
    <td align="right">35.62</td>
    <td align="right">35.50</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.81</td>
    <td align="right">49.01</td>
    <td align="right">49.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">31.62</td>
    <td align="right">32.75</td>
    <td align="right">32.61</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.07</td>
    <td align="right">40.01</td>
    <td align="right">40.16</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.61</td>
    <td align="right">58.25</td>
    <td align="right">58.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.88</td>
    <td align="right">24.34</td>
    <td align="right">27.29</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">32.81</td>
    <td align="right">29.99</td>
    <td align="right">35.88</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">33.02</td>
    <td align="right">34.39</td>
    <td align="right">34.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">31.38</td>
    <td align="right">38.25</td>
    <td align="right">29.13</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">45.86</td>
    <td align="right">39.55</td>
    <td align="right">32.87</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">43.00</td>
    <td align="right">44.58</td>
    <td align="right">44.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">37.63</td>
    <td align="right">44.98</td>
    <td align="right">28.14</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.35</td>
    <td align="right">47.74</td>
    <td align="right">34.32</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">45.97</td>
    <td align="right">46.91</td>
    <td align="right">47.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">42.20</td>
    <td align="right">50.23</td>
    <td align="right">29.71</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">51.34</td>
    <td align="right">52.21</td>
    <td align="right">34.35</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">63.14</td>
    <td align="right">65.28</td>
    <td align="right">64.65</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">107.33</td>
    <td align="right">125.62</td>
    <td align="right">26.92</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">33.92</td>
    <td align="right">53.84</td>
    <td align="right">45.47</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.97</td>
    <td align="right">20.94</td>
    <td align="right">20.84</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">20.00</td>
    <td align="right">24.48</td>
    <td align="right">25.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">87.00</td>
    <td align="right">126.23</td>
    <td align="right">59.43</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.81</td>
    <td align="right">31.85</td>
    <td align="right">31.83</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">24.23</td>
    <td align="right">29.21</td>
    <td align="right">29.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">175.20</td>
    <td align="right">272.53</td>
    <td align="right">84.24</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.00</td>
    <td align="right">42.35</td>
    <td align="right">47.68</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.21</td>
    <td align="right">48.04</td>
    <td align="right">47.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">267.02</td>
    <td align="right">407.85</td>
    <td align="right">97.75</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.75</td>
    <td align="right">62.60</td>
    <td align="right">62.60</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">61.26</td>
    <td align="right">63.75</td>
    <td align="right">64.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.16</td>
    <td align="right">26.44</td>
    <td align="right">26.39</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.47</td>
    <td align="right">35.94</td>
    <td align="right">35.80</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">14.49</td>
    <td align="right">18.80</td>
    <td align="right">18.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.03</td>
    <td align="right">43.16</td>
    <td align="right">43.24</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.42</td>
    <td align="right">45.58</td>
    <td align="right">45.62</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">23.58</td>
    <td align="right">27.04</td>
    <td align="right">27.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.36</td>
    <td align="right">70.10</td>
    <td align="right">72.24</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">103.05</td>
    <td align="right">82.17</td>
    <td align="right">82.38</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">41.32</td>
    <td align="right">45.19</td>
    <td align="right">45.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.82</td>
    <td align="right">93.02</td>
    <td align="right">93.27</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.66</td>
    <td align="right">109.78</td>
    <td align="right">109.83</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">70.02</td>
    <td align="right">74.86</td>
    <td align="right">74.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.08</td>
    <td align="right">16.97</td>
    <td align="right">17.04</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.84</td>
    <td align="right">26.57</td>
    <td align="right">26.52</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.86</td>
    <td align="right">34.39</td>
    <td align="right">33.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">29.47</td>
    <td align="right">27.83</td>
    <td align="right">27.77</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.81</td>
    <td align="right">45.01</td>
    <td align="right">45.13</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">56.49</td>
    <td align="right">54.08</td>
    <td align="right">53.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">54.51</td>
    <td align="right">48.88</td>
    <td align="right">48.10</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">63.88</td>
    <td align="right">69.95</td>
    <td align="right">70.58</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.44</td>
    <td align="right">82.22</td>
    <td align="right">83.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">82.42</td>
    <td align="right">85.12</td>
    <td align="right">83.57</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.90</td>
    <td align="right">93.34</td>
    <td align="right">94.90</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.89</td>
    <td align="right">109.58</td>
    <td align="right">109.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">22.48</td>
    <td align="right">30.23</td>
    <td align="right">31.65</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.77</td>
    <td align="right">35.62</td>
    <td align="right">40.39</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.22</td>
    <td align="right">40.16</td>
    <td align="right">40.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">46.53</td>
    <td align="right">54.98</td>
    <td align="right">39.76</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">62.52</td>
    <td align="right">60.19</td>
    <td align="right">45.99</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">62.91</td>
    <td align="right">58.50</td>
    <td align="right">58.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">67.30</td>
    <td align="right">73.53</td>
    <td align="right">47.78</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">85.24</td>
    <td align="right">85.41</td>
    <td align="right">57.76</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">92.36</td>
    <td align="right">93.83</td>
    <td align="right">93.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">84.76</td>
    <td align="right">90.66</td>
    <td align="right">57.30</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">102.45</td>
    <td align="right">104.21</td>
    <td align="right">66.39</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">142.28</td>
    <td align="right">141.34</td>
    <td align="right">143.71</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.71</td>
    <td align="right">14.03</td>
    <td align="right">8.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">15.87</td>
    <td align="right">22.92</td>
    <td align="right">28.10</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.03</td>
    <td align="right">13.41</td>
    <td align="right">13.35</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.85</td>
    <td align="right">16.22</td>
    <td align="right">16.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.20</td>
    <td align="right">33.81</td>
    <td align="right">28.71</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.32</td>
    <td align="right">16.68</td>
    <td align="right">16.59</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.14</td>
    <td align="right">18.76</td>
    <td align="right">18.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.86</td>
    <td align="right">42.94</td>
    <td align="right">29.37</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.54</td>
    <td align="right">19.10</td>
    <td align="right">19.10</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.66</td>
    <td align="right">21.61</td>
    <td align="right">22.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.73</td>
    <td align="right">59.01</td>
    <td align="right">29.94</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.03</td>
    <td align="right">22.04</td>
    <td align="right">22.04</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.31</td>
    <td align="right">24.43</td>
    <td align="right">24.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.28</td>
    <td align="right">17.18</td>
    <td align="right">17.18</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.11</td>
    <td align="right">17.22</td>
    <td align="right">17.20</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.81</td>
    <td align="right">8.68</td>
    <td align="right">8.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.99</td>
    <td align="right">25.96</td>
    <td align="right">25.96</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.28</td>
    <td align="right">26.18</td>
    <td align="right">26.15</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.06</td>
    <td align="right">12.41</td>
    <td align="right">12.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.41</td>
    <td align="right">36.51</td>
    <td align="right">36.42</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.49</td>
    <td align="right">35.83</td>
    <td align="right">35.67</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.58</td>
    <td align="right">15.40</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.48</td>
    <td align="right">39.02</td>
    <td align="right">39.01</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.29</td>
    <td align="right">40.80</td>
    <td align="right">40.93</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.67</td>
    <td align="right">20.28</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">7.62</td>
    <td align="right">8.49</td>
    <td align="right">8.50</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.28</td>
    <td align="right">17.02</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.15</td>
    <td align="right">17.23</td>
    <td align="right">17.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.97</td>
    <td align="right">12.19</td>
    <td align="right">12.24</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.98</td>
    <td align="right">25.95</td>
    <td align="right">25.95</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.30</td>
    <td align="right">26.18</td>
    <td align="right">26.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.00</td>
    <td align="right">15.33</td>
    <td align="right">15.34</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.40</td>
    <td align="right">36.53</td>
    <td align="right">36.53</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.55</td>
    <td align="right">35.79</td>
    <td align="right">35.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.53</td>
    <td align="right">19.08</td>
    <td align="right">19.09</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.47</td>
    <td align="right">38.92</td>
    <td align="right">38.97</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.35</td>
    <td align="right">40.88</td>
    <td align="right">40.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.07</td>
    <td align="right">18.51</td>
    <td align="right">22.64</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">46.98</td>
    <td align="right">40.78</td>
    <td align="right">40.80</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">26.34</td>
    <td align="right">27.80</td>
    <td align="right">27.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">26.63</td>
    <td align="right">27.54</td>
    <td align="right">23.27</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">51.29</td>
    <td align="right">45.55</td>
    <td align="right">38.70</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">36.11</td>
    <td align="right">34.86</td>
    <td align="right">35.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.28</td>
    <td align="right">34.98</td>
    <td align="right">23.28</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.43</td>
    <td align="right">53.38</td>
    <td align="right">40.35</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.55</td>
    <td align="right">38.04</td>
    <td align="right">37.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">38.46</td>
    <td align="right">45.35</td>
    <td align="right">28.05</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">62.80</td>
    <td align="right">57.29</td>
    <td align="right">42.18</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">51.96</td>
    <td align="right">49.48</td>
    <td align="right">49.43</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">123.78</td>
    <td align="right">61.96</td>
    <td align="right">23.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">19.59</td>
    <td align="right">28.60</td>
    <td align="right">31.71</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">14.30</td>
    <td align="right">15.81</td>
    <td align="right">15.79</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.57</td>
    <td align="right">18.79</td>
    <td align="right">18.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">62.59</td>
    <td align="right">84.36</td>
    <td align="right">43.66</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.46</td>
    <td align="right">27.02</td>
    <td align="right">27.03</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">26.33</td>
    <td align="right">30.77</td>
    <td align="right">31.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">114.84</td>
    <td align="right">158.86</td>
    <td align="right">58.86</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.42</td>
    <td align="right">46.45</td>
    <td align="right">46.43</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">51.41</td>
    <td align="right">52.16</td>
    <td align="right">52.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">166.09</td>
    <td align="right">238.72</td>
    <td align="right">71.72</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.65</td>
    <td align="right">61.77</td>
    <td align="right">61.71</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">66.40</td>
    <td align="right">67.24</td>
    <td align="right">67.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">21.32</td>
    <td align="right">20.98</td>
    <td align="right">21.11</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">18.98</td>
    <td align="right">20.41</td>
    <td align="right">20.41</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">9.91</td>
    <td align="right">10.88</td>
    <td align="right">10.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">32.14</td>
    <td align="right">37.96</td>
    <td align="right">38.03</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.58</td>
    <td align="right">43.68</td>
    <td align="right">43.66</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">19.72</td>
    <td align="right">20.81</td>
    <td align="right">20.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.71</td>
    <td align="right">69.87</td>
    <td align="right">69.88</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.31</td>
    <td align="right">69.26</td>
    <td align="right">69.27</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.73</td>
    <td align="right">37.87</td>
    <td align="right">37.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">88.67</td>
    <td align="right">90.25</td>
    <td align="right">90.26</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.43</td>
    <td align="right">91.24</td>
    <td align="right">91.32</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">51.52</td>
    <td align="right">51.63</td>
    <td align="right">51.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">10.04</td>
    <td align="right">11.20</td>
    <td align="right">11.39</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.16</td>
    <td align="right">22.70</td>
    <td align="right">22.81</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">20.21</td>
    <td align="right">21.56</td>
    <td align="right">21.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">21.52</td>
    <td align="right">23.62</td>
    <td align="right">23.09</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.24</td>
    <td align="right">39.84</td>
    <td align="right">40.56</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.73</td>
    <td align="right">43.25</td>
    <td align="right">43.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">35.88</td>
    <td align="right">38.95</td>
    <td align="right">38.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">66.87</td>
    <td align="right">68.52</td>
    <td align="right">68.60</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.82</td>
    <td align="right">71.01</td>
    <td align="right">70.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.74</td>
    <td align="right">52.02</td>
    <td align="right">52.13</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.68</td>
    <td align="right">87.02</td>
    <td align="right">88.36</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">93.89</td>
    <td align="right">93.18</td>
    <td align="right">93.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">20.81</td>
    <td align="right">21.78</td>
    <td align="right">25.29</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">48.69</td>
    <td align="right">42.00</td>
    <td align="right">42.58</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">37.76</td>
    <td align="right">40.27</td>
    <td align="right">38.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">40.18</td>
    <td align="right">41.49</td>
    <td align="right">30.46</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">67.00</td>
    <td align="right">61.04</td>
    <td align="right">50.79</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">58.18</td>
    <td align="right">56.33</td>
    <td align="right">56.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">60.52</td>
    <td align="right">65.03</td>
    <td align="right">40.10</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">90.26</td>
    <td align="right">85.38</td>
    <td align="right">64.23</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">86.19</td>
    <td align="right">81.05</td>
    <td align="right">81.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">80.43</td>
    <td align="right">87.63</td>
    <td align="right">54.64</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">108.17</td>
    <td align="right">103.88</td>
    <td align="right">74.22</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">130.37</td>
    <td align="right">117.22</td>
    <td align="right">117.22</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.00</td>
    <td align="right">6.65</td>
    <td align="right">5.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">51.48</td>
    <td align="right">44.97</td>
    <td align="right">32.93</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.23</td>
    <td align="right">20.25</td>
    <td align="right">21.64</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.04</td>
    <td align="right">22.52</td>
    <td align="right">24.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">78.10</td>
    <td align="right">66.93</td>
    <td align="right">34.56</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.82</td>
    <td align="right">20.21</td>
    <td align="right">21.60</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.15</td>
    <td align="right">25.08</td>
    <td align="right">26.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">93.31</td>
    <td align="right">79.54</td>
    <td align="right">33.35</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.25</td>
    <td align="right">23.06</td>
    <td align="right">24.35</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.41</td>
    <td align="right">27.68</td>
    <td align="right">28.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">122.14</td>
    <td align="right">100.26</td>
    <td align="right">34.58</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.29</td>
    <td align="right">24.36</td>
    <td align="right">25.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.23</td>
    <td align="right">28.49</td>
    <td align="right">29.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">21.15</td>
    <td align="right">38.26</td>
    <td align="right">38.36</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.56</td>
    <td align="right">38.14</td>
    <td align="right">38.59</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.06</td>
    <td align="right">27.65</td>
    <td align="right">27.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.88</td>
    <td align="right">52.45</td>
    <td align="right">52.43</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">30.07</td>
    <td align="right">52.88</td>
    <td align="right">52.58</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.55</td>
    <td align="right">37.03</td>
    <td align="right">26.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.80</td>
    <td align="right">72.36</td>
    <td align="right">73.50</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.02</td>
    <td align="right">71.93</td>
    <td align="right">72.42</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.53</td>
    <td align="right">54.22</td>
    <td align="right">36.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.73</td>
    <td align="right">81.72</td>
    <td align="right">82.79</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.04</td>
    <td align="right">85.96</td>
    <td align="right">88.71</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">25.56</td>
    <td align="right">54.46</td>
    <td align="right">37.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">16.55</td>
    <td align="right">27.29</td>
    <td align="right">27.03</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.52</td>
    <td align="right">30.05</td>
    <td align="right">29.64</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.20</td>
    <td align="right">29.83</td>
    <td align="right">29.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.55</td>
    <td align="right">44.41</td>
    <td align="right">34.29</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.41</td>
    <td align="right">38.45</td>
    <td align="right">28.83</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.06</td>
    <td align="right">47.27</td>
    <td align="right">37.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.01</td>
    <td align="right">53.59</td>
    <td align="right">36.40</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">29.99</td>
    <td align="right">57.87</td>
    <td align="right">39.86</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.84</td>
    <td align="right">57.74</td>
    <td align="right">39.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.02</td>
    <td align="right">53.77</td>
    <td align="right">36.82</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.15</td>
    <td align="right">59.12</td>
    <td align="right">39.89</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">31.97</td>
    <td align="right">59.12</td>
    <td align="right">39.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">24.69</td>
    <td align="right">41.59</td>
    <td align="right">30.18</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">30.71</td>
    <td align="right">51.55</td>
    <td align="right">33.80</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">34.43</td>
    <td align="right">57.94</td>
    <td align="right">58.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.39</td>
    <td align="right">57.24</td>
    <td align="right">30.73</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">37.97</td>
    <td align="right">58.10</td>
    <td align="right">31.90</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">42.74</td>
    <td align="right">75.54</td>
    <td align="right">78.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">38.37</td>
    <td align="right">70.50</td>
    <td align="right">30.86</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">45.45</td>
    <td align="right">76.72</td>
    <td align="right">33.20</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">45.90</td>
    <td align="right">82.73</td>
    <td align="right">84.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">50.58</td>
    <td align="right">96.12</td>
    <td align="right">31.86</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">54.86</td>
    <td align="right">96.03</td>
    <td align="right">32.99</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">62.56</td>
    <td align="right">113.12</td>
    <td align="right">112.96</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.52</td>
    <td align="right">33.39</td>
    <td align="right">17.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">60.87</td>
    <td align="right">57.21</td>
    <td align="right">38.53</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.03</td>
    <td align="right">20.65</td>
    <td align="right">23.47</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">25.49</td>
    <td align="right">24.84</td>
    <td align="right">26.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">138.19</td>
    <td align="right">148.27</td>
    <td align="right">58.60</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">24.03</td>
    <td align="right">22.80</td>
    <td align="right">24.44</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">32.31</td>
    <td align="right">28.96</td>
    <td align="right">30.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">227.62</td>
    <td align="right">192.49</td>
    <td align="right">59.35</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">35.60</td>
    <td align="right">35.60</td>
    <td align="right">36.66</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">48.84</td>
    <td align="right">49.11</td>
    <td align="right">50.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">362.62</td>
    <td align="right">302.76</td>
    <td align="right">75.10</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">43.02</td>
    <td align="right">43.30</td>
    <td align="right">44.36</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">60.65</td>
    <td align="right">60.32</td>
    <td align="right">62.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.14</td>
    <td align="right">43.80</td>
    <td align="right">44.10</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.34</td>
    <td align="right">45.46</td>
    <td align="right">45.67</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.47</td>
    <td align="right">36.67</td>
    <td align="right">36.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">32.95</td>
    <td align="right">54.66</td>
    <td align="right">54.61</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">46.01</td>
    <td align="right">57.95</td>
    <td align="right">57.73</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.09</td>
    <td align="right">41.10</td>
    <td align="right">30.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">58.02</td>
    <td align="right">88.10</td>
    <td align="right">88.96</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.88</td>
    <td align="right">90.90</td>
    <td align="right">91.43</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">47.89</td>
    <td align="right">80.89</td>
    <td align="right">63.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">74.54</td>
    <td align="right">105.96</td>
    <td align="right">106.79</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.72</td>
    <td align="right">116.27</td>
    <td align="right">118.29</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.98</td>
    <td align="right">92.11</td>
    <td align="right">74.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">16.81</td>
    <td align="right">32.34</td>
    <td align="right">32.28</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">19.12</td>
    <td align="right">31.39</td>
    <td align="right">31.36</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">20.47</td>
    <td align="right">38.61</td>
    <td align="right">38.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">18.53</td>
    <td align="right">49.64</td>
    <td align="right">39.85</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.80</td>
    <td align="right">40.96</td>
    <td align="right">31.22</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">23.49</td>
    <td align="right">51.79</td>
    <td align="right">41.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">48.68</td>
    <td align="right">78.57</td>
    <td align="right">62.39</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">53.18</td>
    <td align="right">84.33</td>
    <td align="right">66.08</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">55.03</td>
    <td align="right">84.78</td>
    <td align="right">66.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">60.56</td>
    <td align="right">92.78</td>
    <td align="right">76.81</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">62.16</td>
    <td align="right">98.02</td>
    <td align="right">78.85</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">64.78</td>
    <td align="right">99.48</td>
    <td align="right">80.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">26.95</td>
    <td align="right">41.75</td>
    <td align="right">32.32</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.67</td>
    <td align="right">55.32</td>
    <td align="right">39.66</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">36.95</td>
    <td align="right">58.37</td>
    <td align="right">58.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">41.24</td>
    <td align="right">66.32</td>
    <td align="right">41.21</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">50.30</td>
    <td align="right">69.45</td>
    <td align="right">45.48</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">54.87</td>
    <td align="right">87.85</td>
    <td align="right">89.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">59.50</td>
    <td align="right">86.03</td>
    <td align="right">47.54</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">72.80</td>
    <td align="right">101.34</td>
    <td align="right">61.12</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">76.16</td>
    <td align="right">103.50</td>
    <td align="right">104.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">80.97</td>
    <td align="right">119.86</td>
    <td align="right">55.57</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">94.37</td>
    <td align="right">130.38</td>
    <td align="right">71.68</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">106.07</td>
    <td align="right">141.04</td>
    <td align="right">141.04</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
